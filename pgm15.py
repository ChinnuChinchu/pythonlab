# check if the input number is prime or not
import math
num = 617
if num > 1:
    for i in range(2, math.ceil(num/2)):
        if (num % i) == 0:
            print(num, "is not a prime number")
            print(i, "times", num//i, "is", num)
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")
# using input() check it is a prime number or not
num = int(input("Enter the number:"))
if num > 1:
    for i in range(2, math.ceil(num/2)):
        if (num % i) == 0:
            print(num, "is not a prime number")
            print(i, "times", num//i, "is", num)
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")

