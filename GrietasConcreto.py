# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 15:13:05 2020

@author: toshiba

Tema: Detectar agrietamiento de concreto.
NOTA: Para obtener el ancho menor de la grita señalada, se puede usar la fórmula: 
                    p = 2*pi*(sqrt(r**2 - s**2) / 2), ya teniendo el perímetro de la imagen recortada
"""
import cv2


umbral = 150
radio = 3
kernel_size = 3

imagen = cv2.imread('img\\Grietas\\grietas_concreto.jpg')
cv2.imshow('Imagen Original', imagen)

gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
bordes = cv2.GaussianBlur(gray, (3,3), 0) #Aplica filtro de distorsión a la imagen
bordes = cv2.Canny(bordes, umbral, umbral*radio, apertureSize = kernel_size)
bordes = cv2.dilate(bordes, None, iterations=1)  # Dilata el contorno de las figuras
bordes = cv2.erode(bordes, None, iterations=1)  # Erosiona el contorno de las figuras
contorno,hierachy = cv2.findContours(bordes, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(imagen, contorno, -1, (0,0,255), 2)


cv2.imshow('Imagen con Deteccion', imagen)
#cv2.imshow('Bordes', bordes)

cv2.waitKey(0)
cv2.destroyAllWindows()


