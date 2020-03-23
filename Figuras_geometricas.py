# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 11:49:47 2020

@author: toshiba

Ejercicio Final: Figuras geométricas: Identificación de polígonos de una imagen.
"""
import cv2

image = cv2.imread('C:\\Users\\toshiba\\Desktop\\Servicio Social\\Python\\Proc_Imagenes\\img\\fig_geometricas.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gray, 10, 150)
canny = cv2.dilate(canny, None, iterations=1)  # Dilata el contorno de las figuras
canny = cv2.erode(canny, None, iterations=1)  # Erosiona el contorno de las figuras

contornos,_ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # Declara los contornos de las figuras

for c in contornos:
    epsilon = 0.01 * cv2.arcLength(c, True)  # Porcentaje de 1%, es arbitrario el número
    approx = cv2.approxPolyDP(c, epsilon, True)  # Argumentos: vector de entrada, porcentaje de lectura, si
                                                                # es una figura cerrada (True/False)
    print(len(approx))
    x,y,w,h = cv2.boundingRect(approx)
    
    if len(approx) == 3:
        cv2.putText(image, 'Triangulo', (x, y), 1, 1, (0,255,0), 1) # Argumentos: imagen, texto, posición en realcióna a la fig., estilo de letra, tamaño, color, "pendiente"
    if len(approx) == 4:
        aspect_ratio = float(w)/h  # Diferencía entre un Cuadrado y un Rectángulo mediante Aspecto de Radio, si la altura entre el ancho son iguales, entonces es Cuadrado 
        print('aspect_ratio=', aspect_ratio)
        if aspect_ratio == 1:
            cv2.putText(image, 'Cuadrado', (x, y), 1, 1, (0,255,0), 1)
        else:
            cv2.putText(image, 'Rectangulo', (x, y), 1, 1, (0,255,0), 1)
    if len(approx) == 5:
        cv2.putText(image, 'Pentagono', (x, y), 1, 1, (0,255,0), 1)
    if len(approx) == 6:
        cv2.putText(image, 'Hexagono', (x, y), 1, 1, (0,255,0), 1)
    if len(approx) > 10:
        cv2.putText(image, 'Circulo', (x, y), 1, 1, (0,255,0), 2)
    
    cv2.drawContours(image, [approx], 0, (0,255,0), 2)
    cv2.imshow('image', image)
    cv2.waitKey(0)

cv2.imshow('image', image)
cv2.imshow('canny', canny)
cv2.waitKey(0)
cv2.destroyAllWindows()

