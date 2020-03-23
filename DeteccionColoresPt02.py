# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 21:11:12 2020

@author: toshiba

Tema: Detección de Colores y Tracking (rastreo).
"""
import cv2
import numpy as np

caption = cv2.VideoCapture(0)

blueBajo = np.array([100,100,20], np.uint8)
blueAlto = np.array([125,255,255], np.uint8)

while True:
    ret,frame = caption.read()
    
    if ret == True:
        frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        maskBlue = cv2.inRange(frameHSV, blueBajo, blueAlto)
        contornos,hierachy = cv2.findContours(maskBlue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        #cv2.drawContours(frame, contornos, -1, (255,0,0), 3)
        
        for c in contornos:  # De cada contorno...
            area = cv2.contourArea(c)  # extrer el área...
            if area > 3000:  # si es mayor a 3000...
                M = cv2.moments(c)  # Indicar y dibujar el punto central de la figura indicada
                if (M["m00"] == 0):  # Si es 0 el denominador, cambiar a 1 por error matemático
                    M["m00"]=1
                
                x = int(M["m10"] / M["m00"])
                y = int(M["m01"] / M["m00"])
                cv2.circle(frame, (x,y), 7, (0,255,0), -1)
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(frame, '{},{}'.format(x,y), (x+10,y), font, 0.75, (0,255,0), 1, cv2.LINE_AA)  # Los paréntesis indican que el valor puede ir cambiando dependiendo las coordenadas del objeto en movimiento
                
                newContorno = cv2.convexHull(c)  # Suaviza el contorno para que no haya picos
                cv2.drawContours(frame, [newContorno], 0, (255,0,0), 3)  # dibujar el contorno tomando [c], (es 0 porque solo se dibujarán los seleccionados, no todos (-1))
        
        #cv2.imshow('Mascara Azul', maskBlue)
        cv2.imshow('Frame', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
caption.release()
cv2.destroyAllWindows()

