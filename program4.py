#Write a function to check if a given number is prime using a loop. For example, is_prime(29) should return True, and is_prime(10) should return False.
def isprime(n):
    if n <= 1:
        return False 
    if n == 2:
        return True   
    if n % 2 == 0:
        return False 
    
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    
    return True
print(isprime(29))  
print(isprime(10))  
