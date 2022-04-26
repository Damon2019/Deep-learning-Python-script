import hdf5storage as hdf5
import numpy as np
import h5py

data1 = np.random.randn(4,4)

hdf5.write(data = data1, path = '/b', filename = './111.jpg', 
           store_python_metadata=True, matlab_compatible=True)

data_read = h5py.File('./train_catvnoncat.h5', 'r')
print(list(data_read.keys()))

