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

def fib():
    init =1
    if times == 0:
        fib = []
    elif times == 1:
        fib = [1]
    elif times == 2:
        fib = [1,1]
    elif times >2:
        fib = [1,1]
        while init <(times-1):
            fib.append(fib[init]+fib[init-1])
            init += 1
    return fib

print(fib())    



# 1+0 = 1 (1,1)
# 1+1 = 2 (1,1,2)
# 1+2 = 3 (1,1,2,3)
# 2+3 = 5 (1,1,2,3,5)
# 3+5 = 8 (1,1,2,3,5,8)
