#Write a function that prints a pattern of stars based on the number of rows provided. For example, if rows = 5, the output should be:
# *
# **
# ***
# ****
# *****

def starPattern(rows):
    for i in range(1, rows + 1):
        print('*' * i)
starPattern(5)
