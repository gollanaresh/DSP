import numpy as n
a=[]
x=input ("enter no of rows-")
y=input ("enter no of columns-")
for i in range(0,x,1):
	z=[]
	for j in range (0,y,1):
		z.append(input("enter a number:"))
	a.append(z)
print a
try:
    inv=n.linalg.inv (a)
except numpy.linalg.LinAlgError:
    pass
else:
    inv=n.linalg.inv (a)
print "Inverse of a given matrix is:\n",inv
