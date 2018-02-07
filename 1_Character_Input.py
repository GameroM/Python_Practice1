## Create a program that asks the user to enter their name and their age. Print
## out a message addressed to them that tells them the year they will turn 100
## years old.

## Extras:
## 1. Add on to the previous program by asking the user for another number and 
## printing out that many copies of the previous message
## 2. Print out that many copies of the previous message on separte lines.
## ( Hint: the string "\n is the same as pressing the enter button)

print('Enter your name')
name = input()
print('Enter your age')
age = int(input())
centi = 2018 - age + 100
message = (name+ ' you will turn 100 in the year '+ str(centi))
print(message)
print('How many times would you like to see the message?')
times = int(input())
for i in range (0,times):
    print(message)
