# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 18:11:17 2020

@author: Marco
"""

import numpy as np
import cv2 
from matplotlib import pyplot as plt

umbral = 165
radio = 3
kernel = np.ones((5,5),np.uint8)
kernel_size = 3

imagen = cv2.imread('img\\Grietas\\grietas_concreto_recortado.jpg')

gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
bordes = cv2.GaussianBlur(gray, (3,3), 0) #Aplica filtro de distorsión a la imagen
bordes = cv2.Canny(bordes, umbral, umbral*radio, apertureSize = kernel_size)
bordes = cv2.morphologyEx(bordes, cv2.MORPH_GRADIENT, kernel) #Elimina lo que hay dentro del contorno

contorno, hierachy = cv2.findContours(bordes, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(imagen, contorno, -1, (255,0,0), 2)

cnt = np.array(contorno) 
cnt = contorno[0]
M = cv2.moments(cnt)
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])

x,y,w,h = cv2.boundingRect(cnt)
cv2.rectangle(imagen,(x,y),(x+w,y+h),(0,255,0),2)
print('Ancho: ', h)

"""
rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
cv2.drawContours(imagen,[box],0,(0,0,255),2)
"""

plt.imshow(imagen)