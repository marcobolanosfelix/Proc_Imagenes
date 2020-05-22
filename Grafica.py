# -*- coding: utf-8 -*-
"""
Created on Thu May 21 17:14:11 2020

@author: Marco
"""

import numpy as np
import matplotlib.pyplot as plt


plt.rcParams.update({'font.size': 20})

x = np.arange(3) # numeros del 0 al 2
y = np.random.rand(3) # llenar "y" con numeros random.

plt.bar(x, y, color=['c', 'b', 'g'])
plt.ylim(0,1) # pone un límite en "y".
plt.grid(True) # pone una "malla".
plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1]) # pone los valores en "y" 



