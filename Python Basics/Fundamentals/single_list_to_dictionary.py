def list_to_dict_1():
    list_1 = [1, 2, 3, 4, 'a', 'b', 'c', 'd']
    # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

    mid = len(list_1)//2
    num = list_1[:mid]
    alpha = list_1[mid:]

    required_dict = {num[i]:alpha[i] for i in range(len(num))}

    print(required_dict)



def list_to_dict_2():
    list_1 = [1, 2, 3, 4, 'e', 'a', 'b', 'c', 'd', 5]
    #expected_output = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}

    numbers = [num for num in list_1 if isinstance(num, (int, float))]
    numbers = sorted(numbers)
    alphabets = [alpha for alpha in list_1 if isinstance(alpha,(str))]
    alphabets = sorted(alphabets)


    required_dict = {numbers[i]:alphabets[i] for i in range(len(numbers))}
    print(required_dict)


# list_to_dict_1()
list_to_dict_2()



