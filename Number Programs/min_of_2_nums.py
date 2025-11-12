def min_version_1(a,b):
    return min(a,b)

def min_version_2(a,b):
    return a if a<b else b

def min_version_3(a,b):
    if a<b:
        return a
    else:
        return b

def min_version_4(a,b):
    call = lambda  a,b: a if a<b else b
    return call(a,b)

def min_version_5(a,b):
    l = []
    l.append(a)
    l.append(b)
    return min(l)

print(f"Minimum of two numbers version 1: {min_version_1(6,9)}")
print(f"Minimum of two numbers version 2: {min_version_2(6,9)}")
print(f"Minimum of two numbers version 3: {min_version_3(6,9)}")
print(f"Minimum of two numbers version 4: {min_version_4(6,9)}")
print(f"Minimum of two numbers version 5: {min_version_5(6,9)}")
