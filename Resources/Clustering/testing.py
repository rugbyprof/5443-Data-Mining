import matplotlib
import matplotlib.pyplot as plt
import numpy as np

import random as pyrand
import tables
matplotlib.rc("image",cmap="gray")

hdf = tables.open_file("leaves.h5","r")
nimages = len(hdf.root.icons)
images = hdf.root.icons[:,:,:]/256.0
data = images.reshape(nimages,-1)



print(data)