# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 18:35:18 2020

@author: toshiba

Tema: Detección de Colores.
Paso 1: Leer el video.
Paso 2: Transformar de BGR a HSV.
Paso 3: Determinar los rangos de color.
Paso 4: Visualización.
"""
import cv2
import numpy as np

caption = cv2.VideoCapture(0)

redBajo1 = np.array([0,100,20], np.uint8)
redAlto1 = np.array([8,255,255], np.uint8)

redBajo2 = np.array([172,100,20], np.uint8)
redAlto2 = np.array([179,255,255], np.uint8)

#blueBajo = np.array([75,100,20])
#blueAlto = np.array([125,255,255])

while True:
    ret,frame = caption.read()
    
    if ret == True:
        frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        maskRed1 = cv2.inRange(frameHSV, redBajo1, redAlto1)
        maskRed2 = cv2.inRange(frameHSV, redBajo2, redAlto2)
        maskRed = cv2.add(maskRed1, maskRed2)
        #maskBlue = cv2.inRange(frameHSV, blueBajo, blueAlto)
    
        #maskRedVista = cv2.bitwise_and(frame, frame, mask=maskRed)
        maskBlueVista = cv2.bitwise_and(frame, frame, mask=maskRed)
        
        cv2.imshow('maskRedVista', maskBlueVista)
        cv2.imshow('mask', maskRed)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
caption.release()
cv2.destroyAllWindows()


