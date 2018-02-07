## Ask the user for a number. Depending on whether the number is even or odd,
## print out and appropiate message to the user. Hint: how does and even/odd
## number react differently when divided by 2?

## Extras:
## If the number is a multiple of 4, print out a different message
## Ask the user for two numbers: one to check(call it num) and one number to
## divide by(check). If check divides evenly into num, tell that to the user.
## If not, print a different appropiate message.


print('Enter a number')
usernum = int(input())
if usernum % 2 == 0 and usernum % 4 == 0:
    print('Number is even and multiple of 4')
elif usernum % 2 == 0:
    print('Number is only even but not a multiple of 4')
else:
    print('Number is odd')


print('Part 2')
print('Enter first number')
a = int(input())
print('Enter second number')
b = int(input())
if a % b == 0:
    print('first number is divisible by second number')
else:
    print('Not divisible')
