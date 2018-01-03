import numpy as np
import random
from scipy import misc
import string


def randomword(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

for i in range(1000):
    data = np.zeros( (50,50, 3), dtype=np.uint8)

    sizeInner = random.randint(4, 36)
    sizeOuter = sizeInner+random.randint(200, 400)

 

    print sizeInner, sizeOuter, i
    filename = random.randint(-1000, 1000)
    #generating the baseplate
    for i in range(50):
        for j in range(50):
            noise = random.randint(-25,25)
            data[i,j] = [100+noise, 100+noise, 100+noise]

    filename = randomword(10)

    img = misc.toimage(data)
    misc.imsave('Examples/Good/'+str(filename)+"_B"+'.jpg', img)
    print "Saving"+filename

