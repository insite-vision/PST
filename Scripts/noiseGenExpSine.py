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

    #Equation for the 2D sine wave exponentialy dampened
    #A*e^{-w*Sqrt(x^2+y^2)}*cos(w*Sqrt(x^2+y^2)+Phi)
    #A est l'amplitude
    #w est la frequence angulaire
    #Phi l'angle de phase
    #A, w, et phi sont choisi aleatoirement
    #TODO: Rajouter un decallage
    for i in range(50):
        for j in range(50):
                A = random.randint(200, 555)
                #w = random.uniform(0,0.2)
                #phi = random.uniform(0, 2)
                A = 600
                w = 0.052
                phi = 1.12
                x = i-24
                y = j-24
                #corriger le premier exp : remplacer w par un delta (decay constant)
                #noise = random.randint(-25,25)
                noise = 0
                result = A*math.exp(-w*math.sqrt(x**2+y**2))*math.cos(w*math.sqrt(x**2+y**2)+phi)
                print "x=",x,"y=",y
                print "x^2+y^2=", x**2+y**2
                data[i,j] = [result+noise, result+noise, result+noise]

    #plt.plot(tab, 'ro')
    #plt.show()
    #print mini, maxi
    filename = randomword(10)
    img = misc.toimage(data)
    plt.imshow(img)
    #plt.show()
    misc.imsave('foo/'+str(filename)+"_G"+'.jpg', img)
    print "[",float(count)/5000.0,"%] Saving "+filename

