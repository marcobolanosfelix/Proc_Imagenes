# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 11:59:28 2020

@author: toshiba

Ejercicio 07: Operadores BITWISE (AND-OR-NOT-XOR).
"""
import cv2
import numpy as np

img1 = np.zeros((400,600), dtype=np.uint8)
img1[100:300, 200:400] = 255
img2 = np.zeros((400,600), dtype=np.uint8)
img2 = cv2.circle(img2, (300,200), 125, (255), -1)

#AND = cv2.bitwise_and(img1, img2)
#cv2.imshow('AND', AND)

#OR = cv2.bitwise_or(img1, img2)
#cv2.imshow('OR', OR)

#NOT = cv2.bitwise_not(img1)
#cv2.imshow('NOT in Cuadrado', NOT)

#NOT = cv2.bitwise_not(img2)
#cv2.imshow('NOT in Circulo', NOT)

#XOR = cv2.bitwise_xor(img1, img2)
#cv2.imshow('XOR', XOR)

cv2.imshow('Cuadrado', img1)
cv2.imshow('Circulo', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()



