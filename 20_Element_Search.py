## Write a function that takes an ordered list of numbers ( a list where the
## elements are in order from smallest to largest) and another number. The function
## decides whether or not the given number is inside the list and returns
## (then prints) an appropiate boolean.



a = [1,3,5,30,42,43,500]
b = int(input('Enter a number:'))

### Without binary search ###

def check():
    if b in a:
        return True
    else:
        return False

print(a)
print(check())


### With binary search ###

def bsearch():
    mid1 = int(len(a)/2)
    compare1 = a[mid1]
    while b <mid1:
     if b < compare1:
        compare2 = a[0:mid1]
        mid2 = int(len(compare2)/2)
        if b < mid2:
            mid3 = int(len2
bsearch()    
