## Write a program that asks the user how many Fibonacci numbers to generate
## and then generates them. Use functions. Make sure to ask the user to enter
## the number of numbes in the sequence to generate. The Fibonacci sequence
## ia a sequence of numbers where the next number in the sequence is the sum of
## the previous two numbers in the sequence. The sequence looks like this:
## (1,1,2,3,5,8,13,21,....)

def get_times():
    return int(input('Enter number of times to\nrun Fibonacci sequence:'))

times = get_times()
#####
#def Fibo():
#    start = 1
#    result = start + start

for num in range(0,times):
 seq = []
 seq.append(1)
 x= seq[0]+0
 seq.append(x)
 y = seq[0]+seq[1]
 seq.append(y)
 z = seq[1]+seq[2]
 seq.append(z)
 a = seq[2]+seq[3]
 seq.append(a)
 print(seq)
    




# 1+0 = 1 (1,1)
# 1+1 = 2 (1,1,2)
# 1+2 = 3 (1,1,2,3)
# 2+3 = 5 (1,1,2,3,5)
# 3+5 = 8 (1,1,2,3,5,8)
# 5+8 = 13 (1,1,2,3,5,8,13)
# 8+13 = 21 (1,1,2,3,5,8,13,21)
# 13+21 = 34 (1,1,2,3,5,8,13,21,34)
    
