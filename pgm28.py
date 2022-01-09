def gcd(x, y):
    while(y):
        x, y = y, x % y
    return x
def lcm(x, y):
    lcm = (x*y)//gcd(x, y)
    return lcm
num1 = 54
num2 = 24
print(lcm(num1,num2))


def gcd(x, y):
    while(y):
        x, y = y, x % y
    return x
def lcm(x, y):
    lcm = (x*y)//gcd(x, y)
    return lcm
num1 =int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
print(lcm(num1,num2))
