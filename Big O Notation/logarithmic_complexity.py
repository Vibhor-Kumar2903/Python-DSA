def logarithmic_complexity(n):
    c = 0
    i = n
    while i > 0:
        c = c + 1
        i = i//2
    return c

print(f"N = 100, number of instruction in O(n) : {logarithmic_complexity(100)}")


