def merge_two_list_as_dict():
    numbers = [1, 2, 3, 4, 5]
    letters = ['a', 'b', 'c', 'd', 'e']

    result = {num:alpha for num,alpha in zip(numbers, letters)}

    print(result)



merge_two_list_as_dict()