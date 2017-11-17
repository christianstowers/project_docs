#collatz conjecture
#page 77

def collatz(n):
    if n % 2 == 0:
        n = n // 2
        return n

    elif n % 2 == 1:
        n = (n * 3) + 1
        return n

n = int(input("Give me a number: "))
while n > 1:
    n = collatz(n)
    print (n)
