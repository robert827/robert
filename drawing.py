# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 16:07:51 2021

@author: AMD_PC
"""

from numpy import log as ln
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import cv2

b = np.load('blue.npy')
g = np.load('green.npy')
r = np.load('red.npy')
e = np.load('rededge.npy')
n = np.load('nir.npy')

a=ln(b+2)
s=ln(g+2)
d=ln(r+2)
f=ln(e+2)
h=ln(n+2)
# 將0項 更改為0.1
#b[b <= 0.0] = 0.1
#g[g <= 0.0] = 0.1
#r[r <= 0.0] = 0.1
#e[e <= 0.0] = 0.1
#n[n<= 0.0] = 0.1


# thermal = np.load('thermal.npy')

# 分離陸地和水
g = cv2.GaussianBlur(g, (75, 75), 0)
n = cv2.GaussianBlur(n, (75, 75), 0)

ndwi = (g-n)/(g+n)  # ndwi


water = ndwi
threshold = 0.35  # 閥值0.23  #####關鍵

water[water > threshold] = 1  # 二值化
water[water < threshold] = 0
water2 = (water+1) % 2
mask = water2 == 1
mx = np.ma.array(water2, mask=mask)
mx = (mx+1) % 2

# 總數據的模型
#do=0.003*1/(blue*red*red)-0.001*1/(red*red*red)-0.001*1/(green*red*red)+0.005*1/(blue*blue*red)-0.018*1/(blue*green*red)+0.013*1/(green*green*red)+0.00017*1/(green*red*rededge)+7.212
#ss=7867.27*ln(ln(nir+2)/(red-ln(green+2)+2))+107451*(red-nir-ln(green+2))-335628*ln(red-nir-ln(green+2)+4)+135.613*(red+0.000001)/(blue+nir)-0.00000108058*ln((blue+nir)/red)-0.00000108071*ln((red+blue)/nir)+242.729*(rededge-ln(rededge+2))*ln(red+2)+480910.92367616534 
#nh3n=0.000480163*1/(green*red*red)-0.000779334*1/(green*green*red)+2.72139*(ln(blue+2))/(red-rededge)-1.41537*(ln(green+2))/(red-rededge)-46.9176*(ln(red+2))/(red-rededge)+49.0598*(ln(rededge+2))/(red-rededge)-0.988969*(ln(blue+2))/(ln(red+2)-ln(rededge+2))-1.42703*(ln(nir+2))/(red-rededge)+24.44026092031006
#bod=46.42969208266938352*(nir+0.000001)/(nir+rededge)-2.902904458851875
#tp=1.74649401212743*(green+rededge)/red-0.195509*ln((green+rededge)/red)-2.899279636797108

# 預測的模型
do=-0.641*b/(r-e)+8.714
ss=-0.0214352/(g*g*e)+86.02703489232249
nh3n=-173.587*ln(e-n-d+4)+208.64728233035962
bod=0.00507904*h/(b-e)+2.2840947354920837
tp=11.0981*ln(h/(e-d+2))-5509.53*(e-n-d)+18201.2*ln(e-n-d+4)-25580.279772735914
# ctis =  82.21412460847752-5.02451*(g/b)


# 濃度分布可視化
size = 2
plt.figure(figsize=(5*size, 5*size))


scale = 255
blurry = 101

plt.subplot(3, 2, 1)
do = cv2.GaussianBlur(do, (blurry, blurry), 0)
do = mx*do
plt.imshow(do, cmap=plt.cm.get_cmap('jet', scale),
           vmin=0, vmax=np.max(do))
plt.title("DO(mg/L)")
plt.colorbar()
plt.axis('off')

plt.subplot(3, 2, 2)
ss = cv2.GaussianBlur(ss, (blurry, blurry), 0)
ss = mx*ss
plt.imshow(ss, cmap=plt.cm.get_cmap('jet', scale),
           vmin=0, vmax=np.max(ss))
plt.title("SS(mg/L)")
plt.colorbar()
plt.axis('off')

plt.subplot(3, 2, 3)
bod = cv2.GaussianBlur(bod, (blurry, blurry), 0)
bod = mx*bod
plt.imshow(bod, cmap=plt.cm.get_cmap('jet', scale),
           vmin=1, vmax=3)
plt.title("BOD(mg/L)")
plt.colorbar()
plt.axis('off')

plt.subplot(3, 2, 4)
nh3n = cv2.GaussianBlur(nh3n, (blurry, blurry), 0)
nh3n = mx*nh3n
plt.imshow(nh3n, cmap=plt.cm.get_cmap('jet', scale),
           vmin=0, vmax=1.5)
plt.title("NH3-N(mg/L)")
plt.colorbar()
plt.axis('off')
#
plt.subplot(3, 2, 5)
tp = cv2.GaussianBlur(tp, (blurry, blurry), 0)
tp = mx*tp
plt.imshow(tp, cmap=plt.cm.get_cmap('jet', scale),
           vmin=0, vmax=0.25)
plt.title("TP(mg/L)")
plt.colorbar()
plt.axis('off')

#河川汙染指數的規定
do[(do >= 6.5) & (do != 3) & (do != 6) & (do != 10) & (do != 0)] = 1.0
do[(6.5 > do) & (4.6 <= do) & (do != 1) & (
    do != 6) & (do != 10) & (do != 0)] = 3.0
do[(4.6 > do) & (2 <= do) & (do != 1) & (
    do != 3) & (do != 10) & (do != 0)] = 6.0
do[(do < 2) & (do >= 0) & (do != 1) & (do != 3) & (do != 6) & (do != 0)] = 10.0
do[do < 0] = 0.0

bod[(bod <= 3.0) & (bod > 0) & (bod != 3.0) & (
    bod != 6) & (bod != 10) & (bod != 0)] = 1.0
bod[(5.0 >= bod) & (3.0 < bod) & (bod != 1) & (
    bod != 6) & (bod != 10) & (bod != 0)] = 3.0
bod[(15.0 >= bod) & (5.0 < bod) & (bod != 1) & (
    bod != 3) & (bod != 10) & (bod != 0)] = 6.0
bod[(bod > 15.0) & (bod != 1) & (bod != 3) & (bod != 6) & (bod != 0)] = 10.0
bod[bod < 0] = 0.0

ss[(ss <= 20.0) & (ss > 0) & (ss != 3.0) & (
    ss != 6) & (ss != 10) & (ss != 0)] = 1.0
ss[(50.0 >= ss) & (3.0 < ss) & (ss != 1) & (
    ss != 6) & (ss != 10) & (ss != 0)] = 3.0
ss[(100 >= ss) & (50.0 < ss) & (ss != 1) & (
    ss != 3) & (ss != 10) & (ss != 0)] = 6.0
ss[(ss > 100.0) & (ss != 1) & (ss != 3) & (ss != 6) & (ss != 0)] = 10.0
ss[ss < 0] = 0.0

nh3n[(nh3n <= 0.5) & (nh3n > 0) & (nh3n != 3.0) & (
    nh3n != 6) & (nh3n != 10) & (nh3n != 0)] = 1.0
nh3n[(1.0 >= nh3n) & (0.5 < nh3n) & (nh3n != 1) & (
    nh3n != 6) & (nh3n != 10) & (nh3n != 0)] = 3.0
nh3n[(3 >= nh3n) & (1.0 < nh3n) & (nh3n != 1) & (
    nh3n != 3) & (nh3n != 10) & (nh3n != 0)] = 6.0
nh3n[(nh3n > 3.0) & (nh3n != 1) & (nh3n != 3)
     & (nh3n != 6) & (nh3n != 0)] = 10.0
nh3n[nh3n < 0] = 0.0




pollution = (do+bod+ss+nh3n)/4
p = pollution
plt.subplot(3, 2, 6)
p = mx*p
bounds=[1,2,3,6,10]
cmap=mpl.colors.ListedColormap(['red','green','blue','yellow'])
norm=mpl.colors.BoundaryNorm(bounds,cmap.N)
plt.imshow(p, cmap=cmap,vmin=1,vmax=10)
plt.title("RPI")
plt.colorbar(
    mpl.cm.ScalarMappable(cmap=cmap,norm=norm),
    spacing='proportional',
    orientation='vertical')
plt.axis('off')
#%%
cmap=mpl.colors.ListedColormap(['red','green','blue','yellow'])
bounds=[1,2,3,6,10]
norm=mpl.colors.BoundaryNorm(bounds,cmap.N)
fig.colorbar(
    mpl.cm.ScalarMappable(cmap=cmap,norm=norm),
    cax=ax,
    spacing='proportional',
    orientation='vertical',
    label='RPI',
    )
    