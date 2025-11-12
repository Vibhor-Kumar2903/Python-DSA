# num = int(input("Enter a number : "))

def isPrime(num):
    factors = 0
    for i in range(1, num+1):
        if num%i==0:
            factors = factors + 1

    return  factors==2

# print(f"Check Prime : {isPrime()}")


def prime_in_a_range():
    num1 = int(input("Enter the starting range : "))
    num2 = int(input("Enter the ending range : "))

    prime_list = []

    for num in range(num1, num2+1):
        if isPrime(num):
            prime_list.append(num)

    return prime_list


print(f"{prime_in_a_range()}")








