## Take two lists, say for example, these two:
## a = [1,1,2,3,5,8,13,21,34,55,89]
## b = [1,2,3,4,5,6,7,8,9,10,11,12,13]
## and write a program that returns a list that contains only the elements that
## are common between the lists(without duplicates). Make sure your program works
## on two lists of different sizes.

## Extras:
## Randomly generate two lists to test this
## Write this in one line of Python
                                    #######
#a = [1,1,2,3,5,8,13,21,34,55,89]
#b = [1,2,3,4,5,6,7,8,9,10,11,12,13]

import random
print('Enter length of first random list')
userin1 = int(input())
print('Enter max value of randomly generated list')
valuein1 = int(input())
a = random.sample(range(valuein1),userin1)

print('Enter length of second random list')
userin2 = int(input())
print('Enter max value of randomly generated list')
valuein2 = int(input())
b = random.sample(range(valuein2),userin2)
print('The first randomly generated list is:', a)
print('The second randmly generated list is:', b)


newlist = []
for numbers in a:
    if numbers in b:
        newlist.append(numbers)
print('The values which repeat are:', newlist)
    
