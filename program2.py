#Write a function to compute the factorial of a given number using a loop. For example, factorial(5) should return 120.
def factorial(n):
    if n < 0:
        return None  # Factorial is not defined for negative numbers
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(factorial(5)) # Taking an example of 5
