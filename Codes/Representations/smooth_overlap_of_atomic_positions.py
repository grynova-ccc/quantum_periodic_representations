# Smooth Overlap of Atomic Positions
from dscribe.descriptors import SOAP
from ase import io
import numpy as np
import pandas as pd
import os
from natsort import natsorted
import glob

lst=[]
for file in natsorted(glob.glob('PATH_TO_CIFS/*.cif')): # Change "PATH_TO_CIFS/*.cif" with your actual folder path
        cif=io.read(file,index=0)
        species = list(set(cif.get_chemical_symbols()))
        rcut = 6.0
        nmax = 8
        lmax = 6
        soap = SOAP(
        species=species,
        periodic=True,
        r_cut=rcut,
        n_max=nmax,
        l_max=lmax)
        s_oap=soap.create(cif, cif.positions).flatten()
        np.save('PATH_TO_OUTPUT_FOLDER/'+file.split('/')[-1].split('.')[0]+'.npy',s_oap) # Change "PATH_TO_OUTPUT_FOLDER/" with your actual folder path
