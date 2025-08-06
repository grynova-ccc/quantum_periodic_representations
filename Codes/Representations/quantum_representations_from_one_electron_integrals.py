# Representations coming from one-electron integrals
from natsort import natsorted
import os
import glob
from sklearn.decomposition import PCA
from joblib import Parallel, delayed

list1=[]
for file in natsorted(glob.glob('PATH_TO_CIFS/*.cif')):
        list1.append(file)


number={0:list1[0:400],1:list1[400:800],2:list1[800:1200],3:list1[1200:1600],4:list1[1600:2000],5:list1[2000:2400],6:list1[2400:2600],
        7:list1[2600:3000],8:list1[3000:3400],9:list1[3400:3600],10:list1[3600:4000],11:list1[4000:4800],12:list1[4800:5200],13:list1[5200:5600],
        14:list1[5600:6000],15:list1[6000:6400],16:list1[6400:6800],17:list1[6800:7200],18:list1[7200:7600],19:list1[7600:8000],20:list1[8000:8400],
        21:list1[8400:9000],22:list1[9000:9400],23:list1[9400:9800],24:list1[9800:10200],25:list1[10200:10600],26:list1[10600:11000],27:list1[11000:]}

def periodic_MAOC(CIF,basis_set='pcseg-0'):
    import numpy as np
    from ase import io
    from pyscf import lo
    from pyscf.pbc import gto
    basis_set=basis_set # Add your selected basis set
    pseudo='gth-pade'
    if type(CIF) is not list:
        print('Add CIFs in a list!')
    else:
        for path in CIF:
            cif=io.read(path,index=0)
            coord=pd.concat([pd.DataFrame(cif.get_chemical_symbols()),pd.DataFrame(cif.get_positions())],axis=1).to_string(header=False,index=False,index_names=False).replace('\n',' ; ') # Extracting actual coordinates from CIFS
            cell = gto.Cell()
            cell.atom = coord
            cell.basis = basis_set
            cell.pseudo = pseudo
            try:
                cell.a = np.eye(3)*cif.cell
            except AttributeError:
                cell.a =cif.cell
            cell.build()
            sm = cell.pbc_intor('int1e_ovlp') # Overlap matrix
            km = cell.pbc_intor('int1e_kin') # kinetic energy matrix
            vm = cell.pbc_intor('int1e_nuc') # Nuclear attraction matrix
            np.save('PATH_TO_OUTPUT_FOLDER_sm/'+path.split('/')[-1].split('.')[0]+'.npy',sm) # Fill "PATH_TO_OUTPUT_FOLDER_sm" with the actual folder path
            np.save('PATH_TO_OUTPUT_FOLDER_km/'+path.split('/')[-1].split('.')[0]+'.npy',km) # Fill "PATH_TO_OUTPUT_FOLDER_km" with the actual folder path
            np.save('PATH_TO_OUTPUT_FOLDER_vm/'+path.split('/')[-1].split('.')[0]+'.npy',vm) # Fill "PATH_TO_OUTPUT_FOLDER_vm" with the actual folder path
    return

results = Parallel(n_jobs=28)(delayed(periodic_MAOC)(number[q]) for q in [x for x in range(0,28,1)])
