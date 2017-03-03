import numpy as np
import imutils
import cv2
import mahotas
#import matplotlib.pyplot as plt
#import matplotlib.image as mpimg
from pylab import *
from mpi4py import MPI
from skimage import data, feature, io
from mahotas.features import surf

comm = MPI.COMM_WORLD

rank = comm.Get_rank()

fname = '/home/ananya/Documents/paradime/data/01.png'
img = io.imread(fname, as_grey=True)

if rank == 0:
    sigmaval=5

if rank == 1:
    sigmaval=10

if rank == 2:
    sigmaval=30

blobs = feature.blob_doh(img, min_sigma=sigmaval, max_sigma=sigmaval)

passpoints = np.zeros((blobs.shape[0], 5))

for i in range(blobs.shape[0]):
        passpoints[i,0],passpoints[i,1],passpoints[i,2] = blobs[i,0], blobs[i,1], blobs[i,2]

desc = surf.descriptors(img, passpoints, is_integral=False, descriptor_only=False)
print passpoints
print desc
#print blobs
#print passpoints



for blob in blobs:
     y, x, r = blob
     scatter(x,y,c='r',s=sigmaval, marker='o')
implot = imshow(img)

show()
