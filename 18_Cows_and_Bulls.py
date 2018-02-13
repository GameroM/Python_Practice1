## Create a program that will play the 'cows and bulls' game with the user. The
## game works like this:
## Randomly generate a 4-digit number. Ask the user to guess a 4 digit number.
## For every digit the user guessed correctly in the correct place, they have a
## cow. For every digit the user guess correctly in the worng place is a bull.
## Every time the user makes a guess, tell them how many cows and bulls they have
## Once the user guesses the correct number, the game is over. Keep track of the
## number of guess the user makes throughout the game and tell the user at the
## end.

import random
 
num1 = str(random.randint(1000,9999)) ## getting random number and making it string
num2 = 'aaaa' ## establishing usernum
cow = 0         ## starting cow counter
bull = 0        ## starting bull counter
counter = 0     ## starting try counter
while num1!= num2:  ## loop for game to keep going if they arent equal
    counter += 1    ## increment by one the coutner for every loop(try)
    num2 = str(input('Please enter your number (between 1000-9999)'))
    for i in range(0,4):    ## to check each digit
        if num1[i] == num2[i]:  ## check each digit
            cow+=1              ## adds cows if equal
        else:
            bull+=1             ## adds bulls if not equal
    print('you have',bull, 'bulls and', cow,'cows')
    cow = bull = 0
else:
    print('Congratulations you guessed it Right and guessed it in', counter,'tries')        

