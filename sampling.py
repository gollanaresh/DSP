import numpy as np
from matplotlib import plt
fs=input("enter a number-)
f=input("enter a number-")
n=np.linspace(0,10,20)
o=np.sin(2*3.14*f*n/fs)
plt.stem(o)
plt.show()
