# Ewald sum matrix
import os
import glob
from natsort import natsorted
import numpy as np
import pandas as pd
from ase import io
from dscribe.descriptors import EwaldSumMatrix

for file in natsorted(glob.glob('PATH_TO_CIFS/*.cif')): # Change "PATH_TO_CIFS/*.cif" with your actual folder path
        cif=io.read(file,index=0)
        atomic_numbers = cif.get_atomic_numbers()
        rcut = 6.0
        nmax = 8
        lmax = 6
        esm = EwaldSumMatrix(
        n_atoms_max=500)
        ewald_sm = esm.create(cif,n_jobs=30)
        np.save('PATH_TO_OUTPUT_FOLDER/'+file.split('/')[-1].split('.')[0]+'.npy',ewald_sm) # Change "PATH_TO_OUTPUT_FOLDER/" with your actual folder path
