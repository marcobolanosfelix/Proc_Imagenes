# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 17:40:04 2020

@author: toshiba

Ejercicio 08: Contando Objetos.
"""
import cv2


imagen = cv2.imread('img\\monedas.jpg')
gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
_,umbral = cv2.threshold(gray, 230, 255, cv2.THRESH_BINARY_INV)
contornos,hierachy = cv2.findContours(umbral, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(imagen, contornos, -1, (255,0,0), 2)
print('Contornos', len(contornos))

cv2.imshow('Original', imagen)
cv2.imshow('Umbral', umbral)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

font = cv2.FONT_HERSHEY_SIMPLEX
i=0

for c in contornos:
    M = cv2.moments(c)
    
    if M["m00"]==0 : 
        M["m00"]=1
        
    x = int(M["m10"] / M["m00"])
    y = int(M["m01"] / M["m00"])
    
    mensaje = 'Num: ' + str(i+1)
    cv2.putText(imagen, mensaje, (x-40,y), font, 0.40, (255,0,0), 2, cv2.LINE_AA)
    cv2.drawContours(imagen, [c], 0, (255,0,0), 2)
    cv2.imshow('Imagen', imagen)
    cv2.waitKey(0)
    i = i+1
    
cv2.destroyAllWindows()
    """
