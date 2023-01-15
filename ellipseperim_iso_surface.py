# -*- coding: utf-8 -*-
"""
Created on 2021 Oct 17
Change log:
    2021 10 19 contour added, code cleaned
    2023 01 15 code reworked
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

def perim(x0, y0): 
# return perimeter according AGM MAGM calc
# parution http://www.ams.org/notices/201208/rtx120801094p.pdf
# author MAGM http://semjonadlaj.com/
#
    if (x0!=0.) and (y0!=0.):
        
        xagm_n = x0
        xagm_N = xagm_n
        yagm_n = y0
        yagm_N = yagm_n
        
        xmagm_n = (x0**2)/math.sqrt((x0**2)+(y0**2))
        xmagm_N = xmagm_n
        ymagm_n = (y0**2)/math.sqrt((x0**2)+(y0**2))
        ymagm_N = ymagm_n
        
        zmagm_n = 0.    # starting at 0 for xmagm and ymagm >=0
        zmagm_N = zmagm_n
    
        while True:
# AGM
            xagm_n = xagm_N
            yagm_n = yagm_N
        
            xagm_N = (xagm_n + yagm_n)/2
            yagm_N = math.sqrt(xagm_n*yagm_n)
            
            convagm = abs(xagm_N-yagm_N)
# MAGM
            xmagm_n = xmagm_N
            ymagm_n = ymagm_N
            zmagm_n = zmagm_N

            xmagm_N = (xmagm_n+ymagm_n)/2
            ymagm_N = zmagm_n + math.sqrt((xmagm_n-zmagm_n)*(ymagm_n-zmagm_n))
            zmagm_N = zmagm_n - math.sqrt((xmagm_n-zmagm_n)*(ymagm_n-zmagm_n))

            convmagm = abs(xmagm_N-ymagm_N)
            
            if ((convagm < 1e-10) and (convmagm < 1e-10)):
                break
                
        Result=4.*math.sqrt((x0**2)+(y0**2))*(xmagm_N/xagm_N)*math.pi/2.
        # perimeter of ellipse
        # (xmagm_N/xagm_N)*math.pi is a so called cosinus elliptique = the same for any equal a/b or b/a
        # and the perimeter of the ellipse will be straight proportional to sqrt((a**2)+(b**2))
        
    else:
        if (x0==0.):
            Result=y0*4
        if (y0==0):
            Result=x0*4
    return Result  

#pdb.set_trace()  # start the debugger

N = 50
Wide = 10.
X = np.arange(0.,Wide,Wide/N)
Y = np.arange(0.,Wide,Wide/N)
Z=np.zeros((N, N))
for i in range(N):
    for j in range(N):
        Z[i,j]=perim((Wide/N)*i, (Wide/N)*j)
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
ax = fig.add_subplot(111, projection='3d')
surf=ax.plot_surface(X,Y,Z, rstride=1, cstride=1, facecolors=fcolors, alpha=0.5, vmin=minn, vmax=maxx, shade=False)
ax.set_xlabel('ellipse halfparam a')
ax.set_ylabel('ellipse halfparam b')
ax.set_zlabel('ellipse perim')
Windo= Wide*2*math.pi
ax.set_zlim(0, Windo)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.01f'))
fig.colorbar(surf, shrink=0.5, aspect=10)
ax.contour(X, Y, Z, 10, linewidths=1.5, cmap="autumn_r", linestyles="solid", offset=-1)
ax.contour(X, Y, Z, 10, linewidths=1.5, colors="k", linestyles="solid")
ax.view_init(elev=20., azim=-100.)
plt.show()
