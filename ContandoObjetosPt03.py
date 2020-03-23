# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 21:39:54 2020
@author: toshiba

Ejercicio 10: Contando Objetos pt.3
"""
import cv2
import numpy as np

def dibujarContorno(contorno, color):
    for(i,c) in enumerate(contorno):
        M = cv2.moments(c)
        if(M['m00']==0): 
            M['m00']=1
        x = int(M['m10'] / M['m00'])
        y = int(M['m01'] / M['m00'])
        cv2.drawContours(imagen, [c], 0, color, 2)
        cv2.putText(imagen, str(i+1), (x+10,y+10), 1, 2, (0,0,0), 2)
        
        
amarilloBajo = np.array([20,100,20], np.uint8)
amarilloAlto = np.array([32,255,255], np.uint8)

violetaBajo = np.array([130,100,20], np.uint8)
violetaAlto = np.array([145,255,255], np.uint8)

verdeBajo = np.array([36,100,20], np.uint8)
verdeAlto = np.array([70,255,255], np.uint8)

azulBajo = np.array([75,100,20], np.uint8)
azulAlto = np.array([125,255,255], np.uint8)

rojoBajo01 = np.array([0,100,20], np.uint8)
rojoAlto01 = np.array([10,255,255], np.uint8)
rojoBajo02 = np.array([175,100,20], np.uint8)
rojoAlto02 = np.array([180,255,255], np.uint8)


imagen = cv2.imread('img\\circulos.png')
imagenHSV = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

maskAmarillo = cv2.inRange(imagenHSV, amarilloBajo, amarilloAlto)
maskVioleta = cv2.inRange(imagenHSV, violetaBajo, violetaAlto)
maskVerde = cv2.inRange(imagenHSV, verdeBajo, verdeAlto)
maskAzul = cv2.inRange(imagenHSV, azulBajo, azulAlto)
maskRojo01 = cv2.inRange(imagenHSV, rojoBajo01, rojoAlto01)
maskRojo02 = cv2.inRange(imagenHSV, rojoBajo02, rojoAlto02)
maskRojo = cv2.add(maskRojo01, maskRojo02)

contornoAmarillo = cv2.findContours(maskAmarillo, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]
contornoVioleta = cv2.findContours(maskVioleta, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]
contornoVerde = cv2.findContours(maskVerde, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]
contornoAzul = cv2.findContours(maskAzul, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]
contornoRojo = cv2.findContours(maskRojo, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]

dibujarContorno(contornoAmarillo, (0,255,255))
dibujarContorno(contornoVioleta, (140,40,120))
dibujarContorno(contornoVerde, (0,255,0))
dibujarContorno(contornoAzul, (255,0,0))
dibujarContorno(contornoRojo, (0,0,255))

cv2.imshow('imagen', imagen)

cv2.waitKey(0)
cv2.destroyAllWindows()


