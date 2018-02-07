## Take two lists, say for example these two:
## a = [1,1,2,3,5,8,13,21,34,55,89]
## b = [1,2,3,4,5,6,7,8,9,10,11,12,13]
## and write a program that returns a list that contains only the elements that are
## common between the lists(without duplicates). Make sure your program works on
## two lists of different sizes. Write this using at least one list comprehension
## Extra: randomly generate two lists to test this


import random

a = [1,1,2,3,5,8,13,21,34,55,89]
b = [1,2,3,4,5,6,7,8,9,10,11,12,13]

#newli = []
#for nums in a:
#    if nums in b:
#        newli.append(nums)
#print(newli)
#x = [nums for nums in a if nums in b]
#print(x)


print('What size list will be randomly generated?')
user1 = int(input())
print('Up to what number would you like to use?')
user1a = int(input())      
c = random.sample(range(0,user1a),user1)
print('The first randomly generated list is:',c)
print('\nWhat size list will be randomly generated?')
user2 = int(input())
print('Up to what number would you like to use?')
user2a = int(input())   
d = random.sample(range(0,user2a),user2)
print('The second randmly generated list is:',d)

x = [nums for nums in c if nums in d]
print('\nThe numbers that coincide in both lists are:',x)
