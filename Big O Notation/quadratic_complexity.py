def quadratic_complexity(n):
    c = 0
    i = 0
    while i < n:
        j = 0
        while j < n:
            c = c + 1
            j = j + 1
        i = i + 1
    return c

print(f"N = 100, number of instruction in O(n^2) : {quadratic_complexity(100)}")


