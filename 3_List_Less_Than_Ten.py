## Take a list, say for example this one:
##  a = [1,1,2,3,5,8,13,21,34,55,89]
## and write a program that prints out all the elements of the list that are less
## than 5. Extras:
## Instead of printing the elements one by one, make a new list that has all the
## elements less than 5 from this list in it and print out this new list
## Write this in one line in Python
## Ask the user for a number a return a list that contains only elements from the
## orignial list 'a' that are smaller than that number given by the user


a = [1,1,2,3,5,8,13,21,34,55,89]

print('Enter a number that will return \n'
      'every number will be smaller than said #')
x = int(input())
newlist = []
for i in a:
    if i < x:
        newlist.append(i)
        
print(newlist)
