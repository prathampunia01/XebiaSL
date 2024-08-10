#Write a function that finds the largest number in a list using a loop. For example, given [4, 7, 1, 8, 3], the output should be 8.

def largestNumber(lst):
    if not lst: 
        return None
    
    largest = lst[0]  
    
    for num in lst:
        if num > largest:
            largest = num
    
    return largest
  
print(largestNumber([4, 7, 1, 8, 3]))
