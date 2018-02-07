## Write a program that takes a list of numbers(for example, a = [5,10,15,20,25])
## and makes a new list of only the first and last elements of the given list.
## Use functions and possibly list comprehension


import random

def get_list():
    max_num = int(input('Enter max number for random list:'))
    max_len = int(input('Enter length of list:'))
    return(random.sample(range(0,max_num),max_len))

#print(get_list())

list1 = get_list()
print(list1)
NL = []

def new_list():   
    first = list1[0]
    last = list1[-1]
    NL.append(first)
    NL.append(last)
    return(NL)

print(new_list())


