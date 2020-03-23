# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 12:15:18 2020

@author: toshiba

Ejercicio 07.2: Operadores BITWISE5.
"""
import cv2
import numpy as np

captura = cv2.VideoCapture(0)
mask = np.zeros((480,640), dtype=np.uint8)
mask = cv2.circle(mask, (320,240), 125, (255), -1)

while (captura.isOpened()):
    ret, frame = captura.read()
    
    if ret == True:
        imgMask = cv2.bitwise_and(frame, frame, mask=mask)
        cv2.imshow('Video', imgMask)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else: 
        break

captura.release()
cv2.destroyAllWindows()    
        
    

