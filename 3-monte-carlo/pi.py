from random import *
from math import sqrt

import matplotlib.pyplot as plt

ins = 0
n = 10000

x_ins = []
y_ins = []
x_outs = []
y_outs = []

for i in range(n):
    x = (random()-0.5)*2
    y = (random()-0.5)*2
    if sqrt(x**2+y**2) <= 1:
        ins += 1
        x_ins.append(x)
        y_ins.append(y)
    else:
        x_outs.append(x)
        y_outs.append(y)

fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.scatter(x_ins,  y_ins, color='g', marker='s')
ax.scatter(x_outs,  y_outs, color='r', marker='s')
plt.show()


pi = 4 * ins / n
print(pi)
