# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 12:30:20 2020

@author: toshiba

Ejercicio 04: Funciones de dibujo.
"""
import cv2
import numpy as np

imagen = 255*np.ones((400,600,3), dtype=np.uint8)

cv2.line(imagen, (0,0), (600,400), (255,0,0), 4)  # Dibuja una línea desde la coordenada (0,0) hasta (600,400) de 
                                                        # color azul con grosor de 4.
cv2.rectangle(imagen, (50,80), (200,200), (0,255,0), 1)  # Dibuja un rectángulo en la posición (50,80) con ancho
                                                            # de 200 y altura de 200, color verde y grosor de 1.
cv2.circle(imagen, (300,200), 100, (0,0,255), 2)  # Dibuja un círculo con punto inicial (300,200), radio de 100,
                                                        # color rojo y grosor 2.
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(imagen, 'Practicando con OpenCV', (10,30), font, 1, (0,255,255), 2, cv2.LINE_AA)  
                                        # Donde se va a visualizar, texto, 
                                            # ubicación, fuente de texto, tamaño del texto 1, 
                                                # color amarillo, grosor 2, tipo de línea.                                                         

cv2.imshow('imagen', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()

