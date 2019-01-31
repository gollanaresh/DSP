print "1st Matrix"
m=input("Enter Row: ")
n=input("Enter Column: ")
a=[[0 for j in range(n)] for i in range(m)]
print ("enter first matrix elements:" )
for i in range(m):
	for j in range(n):
		a[i][j]=input("enter element - ")
print "2nd Matrix"
p=input("Enter Row: ")
q=input("Enter Column: ")
b=[[0 for j in range(q)] for i in range(p)]
print ("enter 2nd matrix elements:" )
for i in range(p):
	for j in range(q):
		b[i][j]=input("enter element - ")
		
print "1st Matrix"
print a
print "2nd Matrix"
print b
if( n!=p):
	print ("matrix multipilication not possible...")
else:
	print ("matix multiplication is possible")
	c=[[0 for j in range(q)] for i in range(m)]
	for i in range(m):
		for j in range(q):
			for k in range(n):
				c[i][j]+=(a[i][k]*b[k][j])
	print ("multiplication of two matrices:")
	print c
	

	
