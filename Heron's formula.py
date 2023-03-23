a = float(input('Please Enter length of first side: '))

b = float(input('Please Enter length of second side: '))

c = float(input('Please Enter length of third side: '))

 

 

s = (a + b + c) / 2

 

triangle_area = (s*(s-a)*(s-b)*(s-c)) ** 0.5

print(' triangle area is : %0.2f' %triangle_area)

