"""Find the largest prime factor of any number."""

def largest_prime_factor(number):
    import math

    """create a function that creates an array of prime values up to square root of the number"""
    prime_values = []
    max_prime_number = sqrt(number)

    for i in range(max_prime_number):
        for j in range(max_prime_number):
            if i % j == 0:
                append.prime_values(j)
    
    print prime_values
    """#a prime number is a value that is not divisible by any number from 2 up to the square root of itself"""


    """reversing the list so that the values are in decending order, we determine the first value that is a factor of the number""" 


largest_prime_factor(10)
