# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 22:51:37 2020

@author: toshiba

Ejercicio: Detectar todas las plantas de agave que halla en la imagen.
"""
import cv2
import numpy as np


blueBajo = np.array([60,100,20])
blueAlto = np.array([95,255,255])

imagen = cv2.imread('C:\\Users\\toshiba\\Desktop\\Servicio Social\\Python\\Proc_Imagenes\\img\\campo_agave.jpg')
imagenHSV = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
maskVerde = cv2.inRange(imagenHSV, blueBajo, blueAlto)


cv2.imshow('imagen', imagen)
cv2.imshow('mask', maskVerde)
cv2.waitKey(0)
cv2.destroyAllWindows()

