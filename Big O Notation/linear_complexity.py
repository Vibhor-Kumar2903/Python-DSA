def linear_complexity(n):
    c = 0
    i = 0
    while i<n:
        c = c + 1
        i = i + 1
    return c

print(f"N = 100, number of instruction in O(n) : {linear_complexity(100)}")


