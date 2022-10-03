# def primes(n):
# <Your code here>
#
# def isPrime(n):
#    if n == 1:
#       return False
#    for t in range(2,n):
#       if n % t == 0:
#          return False
#    return True
#
#
# x=primes()
# print(next(x))
# print(next(x))
# print(next(x))
# Write code for the generator function primes. This function takes one input n, which is the value from which you want
# to start the prime sequence. It returns the prime numbers, no less than the value of n and no greater than 100.
# Please note that you are required to write the function as a generator function.
# When you execute the above code, the output is 2, 3, 5. You are required to use the isPrime function that is provided
# to you above, to check if the current value of n is a prime number.

def primes(n):
# <Your code here>
#
def isPrime(n):
    if n == 1:
       return False
    for t in range(2,n):
       if n % t == 0:
          return False
    return True
#
#
x=primes()
print(next(x))
print(next(x))
print(next(x))