#Write a function to generate the first n Fibonacci numbers using a loop. For example, if n = 6, the output should be [0, 1, 1, 2, 3, 5].

def generate_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fibonacci_sequence = [0, 1]
    
    for i in range(2, n):
        next_fib = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_fib)
    
    return fibonacci_sequence

n = 6
print(generate_fibonacci(n))
