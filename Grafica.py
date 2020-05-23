# -*- coding: utf-8 -*-
"""
Created on Thu May 21 17:14:11 2020

@author: Marco
"""

import numpy as np
import matplotlib.pyplot as plt


lenguajes = ('Python', 'C', 'Java', 'Go', 'JavaScript')
slices = (100, 130, 90, 80, 128)
colores = ('red', 'blue', 'green', '#DD98AA', '#18492D')

_,_,texto = plt.pie(slices, colors=colores, labels=lenguajes, autopct='%1.1f%%')
 
for tex in texto:
    tex.set_color('white')
    
    
plt.axis('equal')
plt.title('Gráfica de Lenguajes de Programación')
plt.show()

