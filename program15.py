#Write a function that takes a list of integers and returns a tuple with the sum of even numbers and the sum of odd numbers. For example, for the list [1, 2, 3, 4, 5, 6], the output should be (12, 9).

def sum_even_odd(lst):
    sum_even = 0
    sum_odd = 0
    
    for num in lst:
        if num % 2 == 0:
            sum_even += num
        else:
            sum_odd += num
    
    return (sum_even, sum_odd)

    result = sum_even_odd([1, 2, 3, 4, 5, 6])
    print(result)
