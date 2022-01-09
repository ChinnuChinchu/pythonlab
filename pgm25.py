# define a function
def computeHCF(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if(x % i == 0) and (y % i == 0):
            hcf = i
    return hcf
num = 54
num2 = 24
print("The H.C.F. of", num, "and", num2, "is", computeHCF(num, num2))
# define a function
def computeHCF(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if(x % i == 0) and (y % i == 0):
            hcf = i
    return hcf
num = int(input("Enter a number:"))
num2 = int(input("Enter the other number:"))
print("The H.C.F. of", num, "and", num2, "is", computeHCF(num, num2))




