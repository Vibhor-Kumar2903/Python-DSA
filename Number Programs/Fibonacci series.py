def fibonacci_series():
    num = int(input("Enter the number : "))
    if num <= 0:
        print("Invalid input..!")
    if num == 1:
        print("Fibonacci series : 1")

    else:
        n1 = 0
        n2 = 1
        count = 0
        print("\nfibonacci series : ")
        while count < num:
            print(n1, end="  ")
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count+=1


fibonacci_series()

