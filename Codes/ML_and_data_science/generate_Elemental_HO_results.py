from joblib import Parallel, delayed
import pandas as pd
import numpy as np
import glob
from qml.math import cho_solve
from qml.kernels import *
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from natsort import natsorted

def KRR(number,path=None,sigma=None,lambd=None,path_results=None):
    '''
    Kernel Ridge Regression with Elemental Hold-Out
    '''
    ele_ho_data={}
    ele_ho_prop={}
    q=0
    for i in natsorted(glob.glob(path+'/*.npy')):
        ele_ho_data[q]=np.load(i)
        ele_ho_prop[q]=pd.read_csv(i.split('.')[0]+'.csv')
        q=q+1
    x=ele_ho_data.pop(number)
    y=ele_ho_prop.pop(number)
    X=np.concatenate(([ele_ho_data[x] for x in list(ele_ho_data)]),axis=0)
    Y=pd.concat([ele_ho_prop[x] for x in list(ele_ho_prop)],axis=0)
    Y=Y['GAP']
    y=y['GAP']
    K=laplacian_kernel(X,X,sigma)
    K[np.diag_indices_from(K)] +=lambd
    alpha=cho_solve(K,Y)
    Ks=laplacian_kernel(x,X,sigma)
    y_pred=np.dot(Ks,alpha)
    results=[]
    results.append(np.mean(np.abs(y_pred-y)))
    results.append(mean_absolute_error(y,y_pred))
    results.append(r2_score(y,y_pred))
    results.append(mean_squared_error(y, y_pred, squared=False))
    A=pd.DataFrame(results)
    A.to_csv(path_results+str(number)+'.csv')
    return

results = Parallel(n_jobs=19)(delayed(KRR)(q) for q in [x for x in range(0,19,1)])
