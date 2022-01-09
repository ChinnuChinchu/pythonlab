# sides of triangle
a = 3
b = 4
c = 5
# calculate the semi-perimeter
s = (a+b+c)/2
# calculate the area
area = (s*(s-a)*(s-b)*(s-c))**0.5
print('The area of the triangle is:', area)
# sides of triangle using input()
x = float(input("Enter the first number:"))
y = float(input("Enter the second number:"))
z = float(input("Enter the third number:"))
sp = float((x+y+z))/2
ar = (sp*(sp-x)*(sp-y)*(sp-z))**0.5
print('The area of the triangle is:', ar)

