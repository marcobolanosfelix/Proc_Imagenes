# -*- coding: utf-8 -*-
"""
Created on Sat May 16 20:22:55 2020

@author: Marco
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

acumulador=0
promedio=0
contador=0
grafica = []
clasificar = ['1er grado', '2do grado', '3er grado']
alto = 0
medio = 0
bajo = 0

imagen = cv2.imread('img\\fracturas.png')
cv2.imshow('Original', imagen)
gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
bordes = cv2.Canny(gray, 100, 200)
bordes = cv2.dilate(bordes, None, iterations=1)  # Dilata el contorno de las figuras
bordes = cv2.erode(bordes, None, iterations=1)  # Erosiona el contorno de las figuras
contorno,hierachy = cv2.findContours(bordes, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(imagen, contorno, -1, (0,0,255), 2)

for c in contorno:
    contador = contador + 1
    distancia = cv2.arcLength(c, True)
    distancia02 = int(distancia)/100 #distancia resultante.
    M = cv2.moments(c)
    if(M["m00"]==0): M["m00"] = 1
    cx = int(M["m10"] / M["m00"])
    cy = int(M["m01"] / M["m00"])
    cv2.putText(imagen, str(distancia02)+'cm', (cx, cy), 1, 1, (0,255,0), 2)
    acumulador = acumulador + distancia02
    
    #obtener el ancho de cada línea.
    rect = cv2.minAreaRect(c)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    cv2.drawContours(imagen,[box],0,(255,0,0),2)
    
    (x, y), (width, height), angle = rect
    aspect_ratio = min(width, height) / max(width, height)
    asp_rat = round(width/10000, 3)
    cv2.putText(imagen, 'Ancho: '+str(width)+'cm', (cx+10,cy+65), 1, 1, (20,117,255), 2)
    cv2.putText(imagen, 'No.'+str(contador), (cx+10,cy+50), 1, 1, (255,0,255), 2)
    
    #Clasificar daño de la fractura.
    if(distancia02 >= 10):
        alto = alto + 1
        print('No.',contador,': Daño grave. Tome medidas !!!',' -> ',distancia02,'cm')
    if(distancia02<10 and distancia02>5):
        medio = medio + 1
        print('No.',contador,': Daño regular. Precaución.',' -> ',distancia02,'cm')
    if(distancia02<=5):
        bajo = bajo + 1
        print('No.',contador,': Daño mnimo.',' -> ',distancia02,'cm')
        
    #Crear gráfica a partir de distancia02
    grafica = grafica + [distancia02]
    
promedio = int(acumulador/len(contorno))    

texto = 'No. Lineas encontrados: '+str(len(contorno))
texto02 = 'Promedio: '+str(promedio)+'cm'
cv2.putText(imagen, texto, (10,20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0), 1)
cv2.putText(imagen, texto02, (10,40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0), 1)
print('No. de Objetos de la imagen: ', len(contorno))

plt.title('= = Clasificación de Fracturas de la Estructura = =')
plt.xlabel('Grado de daño')
plt.ylabel('Longitud (cm)')
plt.plot(grafica)
plt.show()
print(grafica)

cv2.imshow('imagen', imagen)
cv2.imshow('bordes', bordes)

cv2.waitKey(0)
cv2.destroyAllWindows()