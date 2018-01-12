from PIL import Image

from os import listdir
from os.path import isfile, join

files = [f for f in listdir("../Data/PreparedData/") if isfile(join("../Data/PreparedData/", f))]

n = 0

def CheckGrayScale(img):
    img = img.convert('RGB')
    w,h = img.size
    for i in range(w):
        for j in range(h):
            r,g,b = img.getpixel((i,j))
            if (r == 24 and g==255 and b==0):
                return False
    return True

for image in files:
    n += 1
    print "Analysing "+image+"[",n,"/",len(files),"]"

    img = Image.open("../Data/PreparedData/"+image)

    width, height = img.size

    #We cut the image in n*m 96px sized square

    StrideX=48
    StrideY = 48
    numSquareLine = width/StrideX
    numSquareCol = height/StrideY

    print "Width = ", width, "Height =  ", height
    print "Num Squares Line =",numSquareLine,"Num Square Col =", numSquareLine
    print "StrideX=", StrideX, "StrideY=", StrideY
    print "\n"

    for i in range(numSquareCol):
        for j in range(numSquareLine):
            imgCropped = img.crop((j*StrideX, i*StrideY, j*StrideX+96, i*StrideY+96))
            Filename = "PreparedData/"+image+"("+str(j*StrideX)+","+str(i*StrideY)+")("+str(j*StrideX+96)+","+str(i*StrideY+96)+").png"
            imWidth, imHeight = imgCropped.size
            if (imWidth == 96 and imHeight == 96 and CheckGrayScale(imgCropped) == True):
                imgCropped.save(Filename)

