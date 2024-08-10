#Write a function that prints the multiplication table for a given number n up to 10.
def multiplicationTable(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
multiplicationTable(5)
