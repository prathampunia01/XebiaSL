#Write a function to reverse a given string using a loop. For example, for the input "hello", the output should be "olleh".
def reverse_string(s):
    reversed_str = ''
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str
print(reverse_string("hello"))
