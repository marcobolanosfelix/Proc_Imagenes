# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 11:48:41 2020

@author: toshiba

Ejercicio 03: Simple Threshholding (Umbralización).
    Este tema trata de comparar cada pixel de una imagen con el umbral que se requiera (se compara el pixel=35 
        si es mayor a T=210), T=Umbral; si es mayor, el pixel cambia a blanco y si no, a negro. 
"""
import cv2
import numpy as np

imagen = cv2.imread('img\\coins.jpg')
gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

#_,binarizada = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)  # Se compara el cada pixel de la imagen con el Umbral=210
#_,binarizadaInv = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)  # Lo mismo que lo anterior, pero inverso
#_,truncado = cv2.threshold(gray, 100, 255, cv2.THRESH_TRUNC)  # Si es mayor, se muestra el valor del umbral, sino no
_,cero = cv2.threshold(gray, 100, 255, cv2.THRESH_TOZERO)  # Si el pixel es mayor, se toma en cuenta el pixel original, sino el pixel es False
_,ceroInv = cv2.threshold(gray, 100, 255, cv2.THRESH_TOZERO_INV)  # Lo mismo que lo anterior, pero inverso

cv2.imshow('Imagen', gray)
#cv2.imshow('Umbral: Binario - Binario Inv', np.hstack([binarizada, binarizadaInv]))
#cv2.imshow('Umbral: Truncado', truncado)
cv2.imshow('Umbral: To Zero - To Zero Inv', np.hstack([cero, ceroInv]))
cv2.waitKey(0)
cv2.destroyAllWindows()

