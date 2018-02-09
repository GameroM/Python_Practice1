## Write a program(using functions) that asks the user for a long string containing
## multiple words. Print back to the user the same string, except with the words
## in backwwards order. For example, say I type the string:
##  "My name is Michele"
## The result would be:
##  "Michele is name My"

def strininv():
    a = input('Enter a string:')
    b = a.split(' ')
    c= b[::-1]
    d = ' '.join(c)
    return d

print(strininv())
