## Write a program(function) that takes a list and returns a new list that
## contains all the elements of the first list minus all the duplicates.
## Extras
## Write two different functions to do this-one using a loop and constructing a
## list, and another using sets
## Do Exercise 5 with sets and write the solution for that in a different
## function.


a = ['a','b','c','a','b','d']

######## USING FUNCITONS #######
def lisfun():
    newli=[]
    for elem in a:
        if elem not in newli:
            newli.append(elem)
    return newli
     
print(lisfun())

########## USING SETS ##########

#def setfun():
#    setres = set(a)
#    newli = list(setres)
#    return newli

#print(setfun())

