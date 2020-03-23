# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 18:11:25 2020

@author: toshiba

Ejercicio 01: Leer, visualizar y guardar una imagen.
"""

import cv2

imagen = cv2.imread('C:\\Users\\toshiba\\Desktop\\Heroes\\Imagenes\\Paisajes\\Sagas\\viento_saga.jpg', 0) # Lee la imagen y la cambia a gris
resize_img = cv2.resize(imagen, (700 , 400))  # Ajusta el tamaño de la imagen
cv2.imshow('Wind', resize_img)

# cv2.imwrite('viento_saga_gris.jpg', resize_img)  # Guarda la imagen

cv2.waitKey(0)
cv2.destroyAllWindows()

