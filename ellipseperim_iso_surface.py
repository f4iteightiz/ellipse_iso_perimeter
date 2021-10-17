# -*- coding: utf-8 -*-
"""
Created on 2021 Oct 17
draw an isoperimeter surface of ellipse
a and b halfparameter of ellipse (X and Y)
P calculated perimeter (Z)
@author: pascaldagornet at yahoo dot de
under CC BY SA CreativeCommons 4.0
"""
#import pdb # for debugger
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
import math as math

def perim(x, y): # return perimeter according AGM MAGM calc
# http://www.ams.org/notices/201208/rtx120801094p.pdf
    xn=x   
    xN=xn
    yn=y
    yN=yn
    R09=xn*xn+yn*yn
    R10=1.
    if (xn!=0.) and (yn!=0.):
        while True:
            yn=yN
            xn=xN
            yN=math.sqrt(xn*yn)
            R10=R10*2
            xN=xn-(xn-yn)/2
            R09 = R09- R10*((xn-yn)/2)**2
            if (R10*((xn-yn)/2)**2) < 1e-15:
                break
        R09=(R09/yN)*math.pi
    else:
        if (xn==0.):
            R09=yN*4
        if (yn==0):
            R09=xN*4
    return R09  

# domains
#pdb.set_trace()  # start the debugger
N = 50
Wide = 10.
X = np.arange(0.,Wide,Wide/N)
Y = np.arange(0.,Wide,Wide/N)
Z=np.zeros((N, N))
for i in range(N):
    for j in range(N):
        perimeter=perim((Wide/N)*i, (Wide/N)*j)
        Z[i,j]=perimeter
X, Y = np.meshgrid(X, Y)

# fourth dimention - colormap
# create colormap according to x-value (can use any 50x50 array)
color_dimension = Z # change to desired fourth dimension
minn, maxx = color_dimension.min(), color_dimension.max()
norm = matplotlib.colors.Normalize(minn, maxx)
m = plt.cm.ScalarMappable(norm=norm, cmap='jet')
m.set_array([])
fcolors = m.to_rgba(color_dimension)

# plot
fig = plt.figure()
ax = fig.gca(projection='3d')
surf=ax.plot_surface(X,Y,Z, rstride=1, cstride=1, facecolors=fcolors, alpha=0.5, vmin=minn, vmax=maxx, shade=False)
ax.set_xlabel('ellipse halfparam a')
ax.set_ylabel('ellipse halfparam b')
ax.set_zlabel('ellipse perim')
Windo= Wide*2*math.pi
ax.set_zlim(0, Windo)
ax.set_zlim(0, Windo)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.01f'))
fig.colorbar(surf, shrink=0.5, aspect=10)
ax.contour(X, Y, Z, 10, lw=3, cmap="autumn_r", linestyles="solid", offset=-1)
ax.contour(X, Y, Z, 10, lw=3, colors="k", linestyles="solid")
plt.show()