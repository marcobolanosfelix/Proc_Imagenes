# -*- coding: utf-8 -*-
"""
Created on Tue May 12 23:11:58 2020

@author: Marco
"""

# 1st import the package and check its version
import MTM
from MTM import matchTemplates, drawBoxesOnRGB

import cv2
from skimage import io
import matplotlib.pyplot as plt
import numpy as np

image = io.imread('img\\Grietas\\grietas_concreto.jpg')
plt.axis("off")
plt.imshow(image, cmap="gray")

temp0 = image[784:784+400, 946:946+414] # with well 49 
plt.axis("off")
plt.imshow(temp0, cmap="gray")

# 1st format the template into a list of tuple (label, templateImage)
listTemplate = [('temp0', temp0)]
# Then call the function matchTemplates (here a single template)
Hits = matchTemplates(listTemplate, image, N_object=4,score_threshold=0.4, method=cv2.TM_CCOEFF_NORMED, maxOverlap=0.3)

Overlay = drawBoxesOnRGB(image, Hits, boxThickness=5)
plt.figure(figsize = (10,10))
plt.axis("off")
plt.imshow(Overlay)

## Perform rotation of the initial template
listTemplate = [("0", temp0)]

# Initialise figure
f, axarr = plt.subplots(1,3)
axarr[0].imshow(temp0, cmap="gray")

for i,angle in enumerate([90,180]):
    rotated = np.rot90(temp0, k=i+1) # NB: np.rotate not good here, turns into float!
    listTemplate.append( (str(angle), rotated ) )
    axarr[i+1].imshow(rotated, cmap="gray")


Hits = matchTemplates(listTemplate, image, N_object=4, score_threshold=0.4, method=cv2.TM_CCOEFF_NORMED, maxOverlap=0.3)

Overlay = drawBoxesOnRGB(image, Hits, boxThickness=5)
plt.figure(figsize = (10,10))
plt.axis("off")
plt.imshow(Overlay)


