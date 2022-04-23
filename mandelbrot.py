import numpy as np
import matplotlib.pyplot as plt
import math
n = 1000
x = np.linspace(-1.5,1,n)
y = np.linspace(-1,1,n)
outx, outy = [], []
for i in range(len(x)):
    for j in range(len(y)):
        c =  complex(x[i], y[j])
        z=0
        for k in range(20):
            z = z**2 + c
            if math.sqrt(z.real**2 + z.imag**2) > 5:
                outx.append(x[i])
                outy.append(y[j])
                break

        

plt.scatter(outx, outy)
plt.show()
