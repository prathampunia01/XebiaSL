#Write a function that takes an integer and returns the sum of its digits. For example, for the number 1234, the output should be 10 (1 + 2 + 3 + 4).
def sumDigits(n):
    n = abs(n)  
    sumDigits = 0
    
    while n > 0:
        sumDigits += n % 10  
        n //= 10             
    
    return sumDigits
print(sumDigits(123456))
