# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 19:58:34 2020

@author: toshiba

Ejercicio 02: RGB (Red, Green, Blue)
"""
import cv2
import numpy as np

bgr = cv2.imread('img\\violencias_ultraArtefacto.jpg')
bgr2 = cv2.resize(bgr, (400 , 300))

C1 = bgr2[:,:,0]
C2 = bgr2[:,:,1]
C3 = bgr2[:,:,2]
cv2.imshow('BGR', np.hstack([C1,C2,C3]))  # Transformar los canales de Blue, Green y Red

rgb = cv2.cvtColor(bgr2, cv2.COLOR_BGR2RGB)  # Cambia formato de BGR a RGB
C1 = rgb[:,:,0]
C2 = rgb[:,:,1]
C3 = rgb[:,:,2]
cv2.imshow('RGB', np.hstack([C1,C2,C3]))

cv2.waitKey(0)
cv2.destroyAllWindows()

