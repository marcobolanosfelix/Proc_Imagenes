# -*- coding: utf-8 -*-
"""
Created on Fri May 22 19:31:18 2020

@author: Marco
"""

import cv2


imagen = cv2.imread('img\\Grietas\\grietas_concreto.jpg')
img = cv2.resize(imagen, (200,500))
cv2.imshow('imagen',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
