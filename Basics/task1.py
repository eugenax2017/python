import math
a = int(input("Enter leg 1: "))
b = int(input("Enter leg 2: ")) 
c = math.sqrt(a*a + b*b)
print("Hypotenus is: ", c)
# Quadratics
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
print("Quadratic is: %d*x*x + %d*x + %d = 0" % (a,b,c))
dis = b*b - 4*a*c
x1 = x2 = 0
if dis>=0:
	x1 = (-b + math.sqrt(dis))/2*a
	x2 = (-b - math.sqrt(dis))/2*a
	print("x1 = ",x1, "x2 = ",x2)
else:
	print("there's no real solutions")
M = int(input("Enter M: "))
if a<b:
	n1, n2 = a, b
else:
	n1, n2 = b, a
for num1 in range(n1,n2):
	print(num1*M)
input()
