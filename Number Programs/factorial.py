import math

def factorial_1():
    n = int(input("Enter a number : "))
    print(f"Finding factorial of a given number using while loop......")
    fact = 1
    i = 1

    while i<=n:
        fact = fact * i
        i = i + 1
    return fact

def factorial_2(n):
    if n==0:
        return 1
    else:
        return n * factorial_2(n-1)


def factorial_3():
    n = int(input("\nEnter the number : "))
    print(f"Find factorial using inbuilt method ... ")
    print(math.factorial(n))


factorial_1()

print(f"Finding factorial of a given number using recursion : {factorial_2(5)}")

factorial_3()
