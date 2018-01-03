import numpy as np
import matplotlib.pyplot as plt

from matplotlib import cm
from skimage import io
from mpl_toolkits.mplot3d import Axes3D


imArray = io.imread("../Data/Amphi.png", as_grey=True)
imArray = np.array(imArray)


print imArray.shape
##Dipole coord on Amphi.png
##(1655,85),(1749,85)
##(1655,188),(1749,188)
imArray = imArray[85:189,1655:1750]

fig = plt.figure()

ax = fig.gca(projection='3d')

print imArray.shape
print type(imArray)
X = np.arange(0, 103)
Y = np.arange(0, 94)
X, Y = np.meshgrid(X, Y)
Z = imArray[X,Y]
Z /= 50


ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)
plt.show()
