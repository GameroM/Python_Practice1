## Generate a random number betwwen 1 and 9 (including 1 and 9). Ask the user to
## guess the number, then tell them whether they guess too low, too high, or
## exactly right.
## Extras
## Keep going until the user types exit
## Keep track of how many guesses the user has taken and when the game ends, print
## this out.


import random

rand = random.randint(1,9)
print('Random number has been generated')
print('Enter a number from 1 to 9')
counter = 0
while True:
 counter += 1    
 uguess = input()
 if uguess == 'exit':
    break 
 elif int(uguess) > rand:    
    print('Too high, try another number')    
 elif int(uguess) < rand:   
    print('Too low, try another number')
 elif int(uguess) == rand:       
    print('Exactly right, you can type exit to stop now or keep going')
 
 
print('You guessed', counter-1, 'times')

