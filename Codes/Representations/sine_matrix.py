# Sine matrix
import os
import glob
from natsort import natsorted
import numpy as np
import pandas as pd
from ase import io
from dscribe.descriptors import SineMatrix

for file in natsorted(glob.glob('PATH_TO_CIFS/*.cif')): # Change "PATH_TO_CIFS/*.cif" with your actual folder path
        cif=io.read(file,index=0)
        sm = SineMatrix(
        n_atoms_max=500,
        permutation="sorted_l2",
        sparse=False)
        s_m = sm.create(cif, n_jobs=30)
        np.save('PATH_TO_OUTPUT_FOLDER/'+file.split('/')[-1].split('.')[0]+'.npy',s_m) # Change "PATH_TO_OUTPUT_FOLDER/" with your actual folder path
