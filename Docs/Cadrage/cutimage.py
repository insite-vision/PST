#Importation des librairies necessaire
from PIL import Image #Python Image Library

from os import listdir
from os.path import isfile, join

#On recupere les fichiers du repertoire PreparedData
files = [f for f in listdir("../Data/PreparedData/") if isfile(join("../Data/PreparedData/", f))]

n = 0

#Fonction pour verifier si un carre est en noir et blanc
def CheckGrayScale(img):
    img = img.convert('RGB')
    w,h = img.size

    #On itere a travers tous les pixels de l'image
    for i in range(w):
        for j in range(h):
            r,g,b = img.getpixel((i,j))
            if (r == 24 and g==255 and b==0):#Si le pixel contient notre vert alors on renvoie faux

                return False
    return True

for image in files:
    n += 1
    print "Analysing "+image+"[",n,"/",len(files),"]"

    img = Image.open("../Data/PreparedData/"+image)#On ouvre l'image

    width, height = img.size

    #On decoupe l'image en carre de 96*96 avec un recouvrement de moitie

    StrideX=48 #Decallage horizontal du carre
    StrideY=48 #Decallage vertical du carre
    numSquareLine = width/StrideX #Nombre de carre sur une ligne
    numSquareCol = height/StrideY #Nombre de carre sur une colonne

    print "Width = ", width, "Height =  ", height
    print "Num Squares Line =",numSquareLine,"Num Square Col =", numSquareLine
    print "StrideX=", StrideX, "StrideY=", StrideY
    print "\n"

    for i in range(numSquareCol): #On itere de 0 au nombre de carre dans une colonne
        for j in range(numSquareLine): #On itere de 0 au nombre de carre dans une ligne
            
	    #On decoupe l'image en un carre de 96*96, en decallant a chaque fois de 48 pixels horizontalement et verticalement
	    imgCropped = img.crop((j*StrideX, i*StrideY, 
	    j*StrideX+96, i*StrideY+96))

	    #On genere un filename avec les coordoones de l'image
            Filename = "PreparedData/"+image+"("+str(j*StrideX)
	    +","+str(i*StrideY)+")("+str(j*StrideX+96)+","+str(i*StrideY+96)+").png" 
            
	    imWidth, imHeight = imgCropped.size
            
	    #Si la taille de l'image est correcte ET si celle ci ne contient pas de vert, alors on enregistre
	    if (imWidth == 96 and imHeight == 96 and CheckGrayScale(imgCropped) == True):
                imgCropped.save(Filename)
