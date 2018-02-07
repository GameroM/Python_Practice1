## Ask the user for a number and determine whether the number is prime or not.
## (Prime number has no divisor). Use functions to solve.



def get_num():
    return int(input('Enter num:'))

num = get_num()

def check_pri():
    if num %2 == 0:
        return('not prime')
    elif num %3 == 0:
        return(' not prime')   
    elif num %5 == 0:
        return('not prime')    
    elif num %7 == 0:
        return('not prime')
    else:
        return('PRIME')
    
print(check_pri())
    
    
    
    
