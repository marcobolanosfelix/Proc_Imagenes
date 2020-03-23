# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 14:28:39 2020

@author: toshiba

Tema: Detección de grietas de una pared.
"""
import cv2


imagen = cv2.imread('img\\grieta_pared.jpeg')
imagen = cv2.resize(imagen, None, fx=0.6, fy=0.6, interpolation = cv2.INTER_AREA) #Contraer imagen, la original es muy grande
cv2.imshow('Original', imagen)

gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
bordes = cv2.Canny(gray, 100, 200)
bordes = cv2.dilate(bordes, None, iterations=1)  # Dilata el contorno de las figuras
bordes = cv2.erode(bordes, None, iterations=1)  # Erosiona el contorno de las figuras
contorno,hierachy = cv2.findContours(bordes, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(imagen, contorno, -1, (0,0,255), 1)

cv2.imshow('Imagen con Deteccion', imagen)
#cv2.imshow('bordes', bordes)

cv2.waitKey(0)
cv2.destroyAllWindows()


