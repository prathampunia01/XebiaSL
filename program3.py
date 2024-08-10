def sumDigits(n):
    n = abs(n)  
    sumDigits = 0
    
    while n > 0:
        sumDigits += n % 10  
        n //= 10             
    
    return sumDigits
print(sumDigits(123456))
