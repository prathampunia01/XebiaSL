#Write a function that takes a list of integers and returns two lists: one containing all the even numbers and the other containing all the odd numbers.
def separate_even_odd(lst):
    even_numbers = []
    odd_numbers = []
    
    for num in lst:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
    
    return even_numbers, odd_numbers

even, odd = separate_even_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("Even numbers:", even)
print("Odd numbers:", odd)

