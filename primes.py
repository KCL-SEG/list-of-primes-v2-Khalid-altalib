"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = [] #list of primes
    i = 2
    if number_of_primes <= 0:
        raise ValueError("number_of_primes must be a positive integer")
    else:
        while len(list) < number_of_primes: # while the list is less than the number of primes wanted
            for j in range(2,i): # for every number between 2 and i
                if i%j == 0: # if i is divisible by j
                    break
            else:
                list.append(i) # if i is not divisible by any number between 2 and i (its a prime), add it to the list
            i += 1 # increment i
        return list
