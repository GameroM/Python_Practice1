## Make a two player Rock-Paper-Scissors game. (Ask for player plays, compare,
## print out a message of congratulations to the winner, and ask if the players
## want to start a new game.


#print('Would you like to play rock-paper-scissors?')
#respo = input()
while True:
    print('Would you like to play rock-paper-scissors?')
    respo = input()
    if respo == 'yes':
     print('Player 1 make your choice')
     p1c = input()
     print('Player 2 make your choice')
     p2c = input()
     if p1c == 'rock' and p2c == 'rock':
        print('Tie')
     if p1c == 'paper' and p2c == 'paper':
        print('Tie')
     if p1c == 'scissors' and p2c == 'scissors':
        print('Tie')
     if p1c == 'rock' and p2c == 'scissors':
        print('Congrats Player 1 wins!')
     if p1c == 'rock' and p2c == 'paper':
        print('Congrats Player 2 wins!')
     if p1c == 'paper' and p2c == 'scissors':
        print('Congrats Player 2 wins!')
     if p1c == 'paper' and p2c == 'rock':
        print('Congrats Player 1 wins!')
     if p1c == 'scissors' and p2c == 'rock':
        print('Congrats Player 2 wins!')
     if p1c == 'scissors' and p2c == 'paper':
        print('Congrats Player 1 wins!')
     else:
         print('error, try again')
    else:
        break
print('END')
