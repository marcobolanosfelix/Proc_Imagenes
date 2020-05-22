# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 15:11:42 2020

@author: Marco
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

imgL = cv2.imread("C:\\Users\\Marco\\Desktop\\Servicio Social\\Python\\Proc_Imagenes\\img\\lado_der.png", 0)
imgR = cv2.imread("C:\\Users\\Marco\\Desktop\\Servicio Social\\Python\\Proc_Imagenes\\img\\lado_izq.png", 0)

stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
disparity = stereo.compute(imgL, imgR)

plt.imshow(disparity, "gray")
plt.show()
