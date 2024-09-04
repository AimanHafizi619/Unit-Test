import math

def is_prime(num):

    '''Check if num is prime or not.'''
    if type(num) != int:
        raise TypeError("Only integers are allowed")
    
    if num < 0:
        raise ValueError("Negative numbers are not allowed")

    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0: # (2,3), (2,4), (2,5)
            return False
    return True