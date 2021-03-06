# -*- coding: utf-8 -*-
"""animation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1p7Gdad_r2Pk5ourFk1q3rwKV4BKHYTF2
"""
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time
import math
import numpy as np
import imageio

"""-------------------THUẬT TOÁN--------------------"""

#đạo hàm
def grad(x):
    return 2*x+ 5*np.cos(x)
#gốc
def cost(x):
    return x**2 + 5*np.sin(x)
Lx = list()
Ly = list()
def myGD1(eta, x0):
    x = [x0]
    for it in range(100):
        Lx.append(x[-1])
        Ly.append(cost(x[-1]))
        x_new = x[-1] - eta*grad(x[-1])
        if abs(grad(x_new)) < 1e-3:
            break
        x.append(x_new)
    return (x, it)

(x1, it1) = myGD1(.1, -5)
#(x2, it2) = myGD1(.1, 5)
print('Solution x1 = %f, cost = %f, obtained after %d iterations'%(x1[-1], cost(x1[-1]), it1))
#print('Solution x2 = %f, cost = %f, obtained after %d iterations'%(x2[-1], cost(x2[-1]), it2))

"""-------------------BIỂU ĐỒ--------------------"""

x = np.arange(-6,6,0.1)
y = x**2 + 5*np.sin(x)

def draw(i):
    fig = plt.figure()
    ax = plt.axes(xlim=(-6, 6), ylim=(-6, 30))
    plt.plot(x,y, 'b-')
    title = "inter:", i, "cost:", round(Lx[i+1], 2), "grad:", round(Ly[i+1], 2)
    plt.title(title)
    plt.plot(Lx[i],Ly[i],'ko')
    plt.plot(Lx[i+1],Ly[i+1],'ro')
    plt.plot([Lx[i],Lx[i+1]],[Ly[i],Ly[i+1]], 'black')

"""-------------------TẠO GIF--------------------"""

name = "pic"
fullname = ""
fullname_lst = []
path = input(r"nhập path muốn lưu GiF (VD:C:\Users\vinhv\Downloads\ML\animate.gif):")
#path = r"C:\Users\vinhv\Downloads\ML\animate.gif"

for i in range(len(Lx)-1):
    draw(i)
    fullname = name + str(i)
    plt.savefig(fullname)
    fullname_lst.append(fullname + ".png")
    
images = []
for filename in fullname_lst:
    images.append(imageio.imread(filename))
    imageio.mimsave(path, images)




