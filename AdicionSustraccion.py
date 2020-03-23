# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 12:25:38 2020

@author: toshiba

Ejercicio 05: Adición y Sustracción de imágenes.
"""
import cv2

img1 = cv2.imread('C:\\Users\\toshiba\\Desktop\\Servicio Social\\Python\\Proc_Imagenes\img\\coins.jpg')
img2 = cv2.imread('C:\\Users\\toshiba\\Desktop\\Servicio Social\\Python\\Proc_Imagenes\\img\\coca1.jpeg')

resulAdic = cv2.add(img1, img2)  # Adición de las dos imágenes
cv2.imshow('Adición', resulAdic)

resulSub = cv2.subtract(img1, img2)  # Substracción de las dos imágenes
cv2.imshow('Substracción', resulSub)
 
cv2.waitKey(0)
cv2.destroyAllWindows()

