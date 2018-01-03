import numpy as np
import cv2

from matplotlib import pyplot as plt
from os import listdir
from os.path import isfile, join


def auto_canny(image, sigma=0.33):
    # compute the median of the single channel pixel intensities
    v = np.median(image)
             
    # apply automatic Canny edge detection using the computed median
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edged = cv2.Canny(image, lower, upper)
                             
    # return the edged image
    return edged

files = [ f for f in listdir("Data/") if isfile(join("Data/",f))]

for image in files:
    print "Analysing "+image
    img = cv2.imread(".../Data/"+image , 0)
    #auto = auto_canny(img)
    edge = cv2.Canny(img,100,200)

    plt.subplot(121), plt.imshow(img, cmap='gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])

    plt.subplot(122), plt.imshow(edge, cmap='gray')
    plt.title('Edgy Image'), plt.xticks([]), plt.yticks([])

    filename = "output/CANNY_"+image
    plt.savefig(filename)
