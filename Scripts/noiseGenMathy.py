import numpy as np
import random
from scipy import misc
import string
import math
import matplotlib.pyplot as plt
def randomword(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

count = 0
for i in range(5000):
    count += 1
    data = np.zeros( (50,50, 3), dtype=np.uint8)



   # generating the baseplate
    for i in range(50):
        for j in range(50):
            noise = random.randint(-25,25)
            data[i,j] = [100+noise, 100+noise, 100+noise]

    dampener = 1.0/random.randint(25, 35)
    scalingFactor = (10.0*random.uniform(10,20))
    print dampener
    #generating inner circle
    #Equation for the Dipole noise
    #Sin[Log[((x - 24)^2 + (y - 24)^2)]
    for i in range(50):
        for j in range(50):
                #scalingFactor     = (10.0*random.uniform(0.5,2.5))
                #numeratorFactor   = (10.0*random.uniform(0.5,2.5))
                #denominatorFactor = (1.0/random.uniform(0.5,2.5))
                #scalingFactor =1.0  
                #dampener = 1.0
                #reduction = random.randint(-75, -25)
                x = i-24
                y = j-24
                noise = random.randint(-25,25)
                #noise = 0 
                #result = math.sin(numeratorFactor*math.sqrt((x**2+y**2)))/(denominatorFactor*math.sqrt((x**2+y**2))) - reduction
                try:
                    result = math.exp(math.sin(dampener*math.pi*math.sqrt((x**2+y**2)))/(dampener*math.pi*math.sqrt((x**2+y**2))))*scalingFactor
                    if result < 0:
                        result = 0
                    print result
                except ZeroDivisionError:
                    result = 0
                #data[i,j] = [result*scalingFactor+noise, result*scalingFactor+noise, result*scalingFactor+noise]
                data[i,j] = [result+noise, result+noise, result+noise]
                #data[i,j] = [result, result, result]

    #plt.plot(tab, 'ro')
    #plt.show()
    #print mini, maxi
    filename = randomword(10)
    img = misc.toimage(data)
    plt.imshow(img)
    #plt.show()
    misc.imsave('foo/'+str(filename)+"_G"+'.jpg', img)
    print "[",float(count)/5000.0,"%] Saving "+filename

