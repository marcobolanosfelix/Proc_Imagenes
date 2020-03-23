# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 19:12:41 2020

@author: toshiba

Ejercicio 06: Contornos y cómo dibujarlos.
"""
import cv2


imagen = cv2.imread('img\\fig_contornos.png')
gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
_,umbral = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

contornos,hierachy = cv2.findContours(umbral, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # Argumentos: umbral, modo de contornos, tipo de contorno (recomendada esta)
cv2.drawContours(imagen, contornos, -1, (0,255,0), 3) # Argumentos: imagen, contornos, (si es negativo abarca todas las figuras), color, grosor

cv2.imshow('Umbral', umbral)
cv2.imshow('imagen', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()
