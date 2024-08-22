import math

def product_of_numbers_upto_n(n):
    return math.prod(range(1, n+1))

n = 5
print(f"Product of numbers up to {n} is: {product_of_numbers_upto_n(n)}")

#Divide Each Number by All Numbers up to n-1 and Check Whether It is Prime

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def divide_and_check_prime(n):
    primes = []
    for num in range(2, n):
        if is_prime(num):
            primes.append(num)
    return primes

n = 10
print(f"Prime numbers less than {n} are: {divide_and_check_prime(n)}")

# Code to Give All Factors of a Number (For All Numbers from 1 to 100)
def factors_of_number(num):
    return [i for i in range(1, num + 1) if num % i == 0]

def factors_of_all_numbers_upto_100():
    for num in range(1, 101):
        print(f"Factors of {num}: {factors_of_number(num)}")

factors_of_all_numbers_upto_100()

#Multiply All Prime Numbers up to n
def multiply_primes_upto_n(n):
    product = 1
    for num in range(2, n+1):
        if is_prime(num):
            product *= num
    return product

n = 10
print(f"Product of all prime numbers up to {n} is: {multiply_primes_upto_n(n)}")
#Take Three Numbers as Input (3D Vector) and Output the Distance from (0, 0, 0)
import math

def vector_distance(x, y, z):
    return math.sqrt(x**2 + y**2 + z**2)

# Example inputs
x, y, z = 3, 4, 5
print(f"The distance of the vector ({x}, {y}, {z}) from (0, 0, 0) is: {vector_distance(x, y, z)}")



