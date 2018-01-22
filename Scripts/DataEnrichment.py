from PIL import Image

import numpy as np

from os import listdir
from os.path import isfile, join

files = [f for f in listdir("dipoles/") if isfile(join("dipoles/", f))]

n = 0

print "s"

for image in files:
    n+=1
    print "Analysing "+image+"[",n,"/",len(files),"]"
   
    #On a 5 transformations simples:
    #Rotations par Pi/2, pi, 3/2pi
    #Miroir sur axe x, axe y
    #On a donc 8 image uniques que nous pouvons produire
    #6 sont accessible avec une seule transformation
    #2 le sont en enchainent 1 rot et 1 miroir
    #Plus de transformations ne produisent que des exemples deja vu
    
    #Rotation
    img = Image.open("dipoles/"+image)
    img.rotate(90).save("Enriched/90"+image)
    img.rotate(180).save("Enriched/180"+image)
    img.rotate(270).save("Enriched/270"+image)
    

    #Miroir
    img.transpose(Image.FLIP_TOP_BOTTOM).save("Enriched/FlipY"+image)
    img.transpose(Image.FLIP_LEFT_RIGHT).save("Enriched/FlipX"+image)
    Flip = img.transpose(Image.FLIP_LEFT_RIGHT)

    #Double transfo
    Flip.rotate(90).save("Enriched/F90"+image)
    Flip.rotate(180).save("Enriched/F180"+image)
    
