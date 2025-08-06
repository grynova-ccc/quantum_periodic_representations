# Local Many-body Tensor Representation
import os
import glob
from natsort import natsorted
import numpy as np
import pandas as pd
from ase import io
from dscribe.descriptors import LMBTR

for file in natsorted(glob.glob('PATH_TO_CIFS/*.cif')): # Change "PATH_TO_CIFS/*.cif" with your actual folder path
        cif=io.read(file,index=0)
        lmbtr = LMBTR(
        species=list(set(cif.get_chemical_symbols())),
        geometry={"function": "distance"},
        grid={"min": 0, "max": 5, "n": 100, "sigma": 0.05},
        weighting={"function": "exp", "scale": 0.5, "threshold": 0.0005},
        periodic=True,
        normalization="l2",)
        l_mbtr = lmbtr.create(cif, n_jobs=30)
        np.save('PATH_TO_OUTPUT_FOLDER/'+file.split('/')[-1].split('.')[0]+'.npy',l_mbtr) # Change "PATH_TO_OUTPUT_FOLDER/" with your actual folder path
