import numpy as np
import cv2

from matplotlib import pyplot as plt
from os import listdir
from os.path import isfile, join

files = [ f for f in listdir("../Data/") if isfile(join("../Data/",f))]

for image in files:
    print "Analysing "+image
    img = cv2.imread("../Data/"+image , 0)
    edge = cv2.Canny(img,100,200)

    plt.subplot(121), plt.imshow(img, cmap='gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])

    plt.subplot(122), plt.imshow(edge, cmap='gray')
    plt.title('Edgy Image'), plt.xticks([]), plt.yticks([])

    filename = "output/CANNY_"+image
    plt.savefig(filename)
