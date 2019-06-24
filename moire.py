import matplotlib.pyplot as plt 
import numpy as np
from math import pi

fig, axes = plt.subplots(1, 1)
t = np.linspace(0, pi, 5000)
x = np.cos(t) + np.cos(105*t)/2 + np.sin(100*t)/3  
y = np.sin(t) + np.sin(105*t) + np.cos(100*t)/3

axes.plot(x, y)
axes.axis('equal')
plt.show()
