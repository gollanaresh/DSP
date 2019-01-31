import numpy as np
from matplotlib import plt
fs1=input("enter a number-")
f1=input("enter a number-")
n=np.arange(0,2000,0.1)
a1=np.sin(2*3.14*f1*n/fs1)
plt.plot(a1)
plt.show()
fs2=input("enter a number-")
f2=input("enter a number-")
n2=np.arange(0,2000,0.1)
a2=np.sin(2*3.14*f2*n2/fs2)
plt.plot(a2)
plt.show()
y=a1+a2
print("y")
plt.plot(y)
plt.show()
