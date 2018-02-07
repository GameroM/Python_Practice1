## Create a program that asks the user for a number and then prints out a list of
## all the divisors of that number. (For example, 13 is a divisor of 26, or
## 3 is a divisor of 21 because there is no remainder)

print('Enter a number to recieve its divisors')
a = int(input())
x = range(1,a+1)
for elem in x:
    if a % elem == 0:
        print(elem)
    
