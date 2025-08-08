import pandas as pd
import numpy as np
import glob
import sys
from sklearn.decomposition import PCA
from pyscf import scf,gto,lo
from qml.math import cho_solve
from qml.kernels import *
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from natsort import natsorted
from sklearn.metrics import mean_squared_error
from master_strange_mol_rep.mol_rep import zero_pad_two_ndarrays as pad
from sklearn.model_selection import KFold

#optimize sigma is a function that optimises the sigma and lambda hyperparameter values. 
def optimize_sigma(data=None,target=None,split=2,kernel='Laplacian',min_sigma=1,step=1000,max_sigma=10000,shuffle=True):
    eta = np.logspace(-10, 0, 5)
    ert_mae=[]
    ert_nr=[]
    for t in eta:
        Z=pd.concat([pd.DataFrame(data),pd.DataFrame(target)],axis=1)
        kf = KFold(n_splits=split, shuffle=shuffle,random_state=137)
        kf.get_n_splits(Z)
        tab=[]
        for train_index, test_index in kf.split(Z):
            mae=[]
            nr=[]
            X_train = Z.iloc[train_index].drop(list(Z.iloc[train_index].iloc[:,-1:]),axis=1)
            X_test = Z.iloc[test_index].drop(list(Z.iloc[test_index].iloc[:,-1:]),axis=1)
            y_train = Z.iloc[train_index].iloc[:,-1:][list(Z.iloc[train_index].iloc[:,-1:])[0]]
            y_test = Z.iloc[test_index].iloc[:,-1:][list(Z.iloc[test_index].iloc[:,-1:])[0]]
            for i in range(min_sigma,max_sigma,step):
                if kernel == 'Laplacian':
                    K=laplacian_kernel(X_train,X_train,i)
                    K[np.diag_indices_from(K)] +=t
                    v=np.mean(np.abs(np.dot(laplacian_kernel(X_test,X_train,i),cho_solve(K,y_train))-y_test))
                else:
                    K=gaussian_kernel(X_train,X_train,i)
                    K[np.diag_indices_from(K)] +=t
                    v=np.mean(np.abs(np.dot(gaussian_kernel(X_test,X_train,i),cho_solve(K,y_train))-y_test))
                mae.append(v)
                nr.append(i)
            A=pd.DataFrame(mae,columns=['mae'])
            B=pd.DataFrame(nr,columns=['Nr'])
            C=pd.concat([A,B],axis=1)
            tab.append(C)
        ert_mae.append((sum(tab)/len(tab)).loc[(sum(tab)/len(tab))['mae'] == (sum(tab)/len(tab))['mae'].min()]['mae'])
        ert_nr.append((sum(tab)/len(tab)).loc[(sum(tab)/len(tab))['mae'] == (sum(tab)/len(tab))['mae'].min()]['Nr'])
    return (ert_mae, ert_nr,eta)

A=np.load(INPUT_DATA_PATH)[:3000]
B=pd.read_csv(OUTPUT_DATA_PATH)['GAP'][:3000]

Q=optimize_sigma(data=A,target=B,split=4)
print(Q)
