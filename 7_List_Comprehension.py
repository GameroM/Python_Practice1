## Lets say I give you a list saved in a variable:
## a = [1,4,9,16,25,36,49,64,81,100].
## Write one line of Python that takes this list and makes a new list that has
## only even elements of this list in it.


a = [1,4,9,16,25,36,49,64,81,100]
even = [ enumbs for enumbs in a if enumbs %2 == 0]
print(even)

#newev = []
#for numbs in a:
#    if numbs % 2 ==0:
#        newev.append(numbs)
#print(newev)
    
