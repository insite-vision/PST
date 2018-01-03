import numpy as np
import random
from scipy import misc
import cv2

from os import listdir
from os.path import isfile, join

files = [ f for f in listdir("Examples/") if isfile(join("Examples/", f))]

output =[]
y_data =[]
#examples = random(examples, len(examples))
for i in files:
    img = cv2.imread("Examples/"+i, 0)
    print i
    if img is not None:
        output.append(img)
        if i.endswith('G.jpg'):
            y_data.append(1)
        elif i.endswith('B.jpg'):
            y_data.append(0)


print y_data



