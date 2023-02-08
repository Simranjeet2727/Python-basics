#Program to find the area of triangle

#to take inputs from the user
a = float(input('Enter first side: '))
b = float(input('Enter second side: '))
c = float(input('Enter third side: '))

# calculate the semi-perimeter
s = (a + b + c) / 2
print("semi-perimeter = ",s)

# calculate the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print("area of trinagle = ",area)
print('approx. area of the triangle is %0.2f' %area)