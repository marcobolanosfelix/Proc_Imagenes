# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 12:29:00 2020

@author: toshiba

Ejercicio 09: Contando Objetos pt.2
"""
import cv2
import numpy as np

imagen = cv2.imread('C:\\Users\\toshiba\\Desktop\\Servicio Social\\Python\\Proc_Imagenes\\img\\cartas.jpg')
gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
bordes = cv2.Canny(gray, 100, 200)
contornos,hierachy = cv2.findContours(bordes, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(imagen, contornos, -1, (0,0,255), 2)

texto = 'No. Contornos encontrados: '+str(len(contornos))
cv2.putText(imagen, texto, (10,20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0), 1)
print('No. de Objetos de la imagen: ', len(contornos))

cv2.imshow('imagen', imagen)
cv2.imshow('bordes', bordes)

cv2.waitKey(0)
cv2.destroyAllWindows()

