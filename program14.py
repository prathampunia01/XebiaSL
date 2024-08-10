#Write a function that prints all multiples of a given number up to a specified limit. For example, for num = 3 and limit = 20, the output should be 3, 6, 9, 12, 15, 18.

def print_multiples(num, limit):
    multiples = []
    multiple = num
    while multiple <= limit:
        multiples.append(multiple)
        multiple += num
    print(', '.join(map(str, multiples)))
  
print_multiples(3, 20)
