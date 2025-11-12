def is_anagram():
    str1 = input(f"Enter first string : ")
    str1 = str1.lower()
    str2 = input(f"Enter second string : ")
    str2 = str2.lower()
    print(f"Given strings are - \n String 1 : {str1} \n String 2 : {str2}")

    if len(str1) == len(str2) and sorted(str1) == sorted(str2):
        print("This is Anagram.")

    else:
        print("Not an Anagram.")

is_anagram()
