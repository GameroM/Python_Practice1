## Write a password generate in Python. Be creative with how you generate
## passwords - strong passwords have a mix of lowercase letters, numbers, and
## symbols. The passowrd should be random, generating a new password every time
## the user asks for a new password. Include your run-tim code in a main method.
## Extra:
## Ask the user how strong they want their passowrd to be. For weak passowrds,
## pick a word or two from a list


import random

askstr = input('How strong would you like the password to be?'
          '\nhard, medium or weak?:') 
def passgeneasy():
    passwords = ['one','two','three','four','five']
    x = input('pick from this list: [one,two,three,four,five]:\n')
    if x == 'one':
        return passwords[0]
    if x == 'two':
        return passwords[1]
    if x == 'three':
        return passwords[2]
    if x == 'four':
        return passwords[3]
    if x == 'five':
        return passwords[4]
    
#print(passgeneasy())
        
def passgenmed():
    a = int(input('Enter length of medium strength password, up to 9 chars: '))
    b= random.sample(['a','b','c','d','1','2','3','4','5'],a)
    c = "".join(b)
    return c
#print(passgenmed())

def passgenhard():
    a = int(input('Enter length of hard strength password, up to 22 chars: '))
    b= random.sample(['a','b','c','d','1','2','3','4','5','A','B','C','D','E','F','G','!','@','#','$','%','&'],a)
    c = "".join(b)
    return c    
#print(passgenhard())

def passgenfinal():
 if askstr == 'weak':
    return passgeneasy()
 elif askstr == 'medium':
    return passgenmed()
 elif askstr == 'hard':
    return passgenhard()
 else:
    return('ERROR')

print('Your password is:',passgenfinal())
