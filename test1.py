import numpy as np
from matplotlib import pyplot as plt
x=np.linspace(-5,5,200)
fig1=plt.figure(figsize=(10,5))
ax=plt.subplot()
ax.plot(x,x*x+2*x+1,c='r',linewidth=4)
ax.set_title("$x^2+2x+1$")
plt.show()