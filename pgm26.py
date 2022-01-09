def computeHCF(x, y):
    while(y):
        x, y =  y, x % y
    return x
print(computeHCF(300, 400))



def computeHCF(x, y):
    while(y):
        x, y =  y, x % y
    return x
n = int(input("1st num:"))
n2 = int(input("2nd num:"))
print(computeHCF(n, n2))
