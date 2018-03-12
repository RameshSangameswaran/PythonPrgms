#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 09:10:48 2018

@author: user
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 10)
y = 2.5 * (x - 0.1) + 0.75

plt.plot(x, y)
plt.show()