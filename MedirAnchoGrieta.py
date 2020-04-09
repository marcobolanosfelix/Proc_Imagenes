# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 12:51:33 2020

@author: toshiba
Tema: Detectar borde y obtener el ancho de una grieta.
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt


umbral = 165
radio = 3
kernel = np.ones((5,5),np.uint8)
kernel_size = 3

imagen = cv2.imread('img\\Grietas\\grietas_concreto_recortado.jpg');

plt.imshow(imagen)

gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
bordes = cv2.GaussianBlur(gray, (3,3), 0) #Aplica filtro de distorsión a la imagen
bordes = cv2.Canny(bordes, umbral, umbral*radio, apertureSize = kernel_size)
bordes = cv2.morphologyEx(bordes, cv2.MORPH_GRADIENT, kernel) #Elimina lo que hay dentro del contorno

#bordes = cv2.dilate(bordes, None, iterations=1)  # Dilata el contorno de las figuras
#bordes = cv2.erode(bordes, None, iterations=1)  # Erosiona el contorno de las figuras
#bordes = cv2.morphologyEx(bordes, cv2.MORPH_OPEN, kernel)
#bordes = cv2.bilateralFilter(bordes, 9, 75, 75)
contorno, hierachy = cv2.findContours(bordes, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


cv2.drawContours(imagen, contorno, -1, (0,0,255), 2)
ctn = np.array(contorno) 
ctn = contorno[0]
M = cv2.moments(ctn)
#x,y,w,h = cv2.boundingRect(contorno)
#imagen = cv2.rectangle(imagen,(x,y),(x+w,y+h),(0,255,0),2)
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])
#ancho = ctn.shape
#print(ancho)
"""
rect = cv2.minAreaRect(contorno)
box = cv2.cv.BoxPoints(rect) # cv2.boxPoints(rect) for OpenCV 3.x
box = np.int0(box)
cv2.drawContours(imagen,[box],0,(0,0,255),2)
"""
#texto = 'Ancho de la Grieta: '+str(w)
#cv2.putText(imagen, texto, (10,20), cv2.FONT_HERSHEY_SIMPLEX, 0.2, (255,0,0), 1)

plt.imshow(imagen)
cv2.imshow('Imagen', imagen)    

cv2.waitKey(0)
cv2.destroyAllWindows()

