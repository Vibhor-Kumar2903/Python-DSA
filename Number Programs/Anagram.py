def is_numbers_are_anagram():
    num1 = int(input(f"Enter first digit : "))
    str1 = str(num1)
    num2 = int(input(f"Enter second digit : "))
    str2 = str(num2)
    print(f"Given digits are - \n Number 1 : {str1} \n Number 2 : {str2}")

    if len(str1) == len(str2) and sorted(str1) == sorted(str2):
        print("This is Anagram.")

    else:
        print("Not an Anagram.")

is_numbers_are_anagram()