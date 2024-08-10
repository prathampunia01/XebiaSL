#Write a function that prints a number pattern based on a given integer n. For example, for n = 4, the output should be:
# 1
# 22
# 333
# 4444

def print_number_pattern(n):
    for i in range(1, n + 1):
        print(str(i) * i)
print_number_pattern(4)
