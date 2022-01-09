# check given number is positive or negative
num = float(input('Enter the number:'))
if num >= 0:
    if num == 0:
        print('Zero')
    else:
     print(num, 'is a Positive number')
else:
    print(num, 'is a Negative number')
