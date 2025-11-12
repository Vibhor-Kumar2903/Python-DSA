def max_version_1(a,b):
    return max(a,b)

def max_version_2(a,b):
    return a if a>b else b

def max_version_3(a,b):
    if a>b:
        return a
    else:
        return b

def max_version_4(a,b):
    call = lambda  a,b: a if a>b else b
    return call(a,b)

def max_version_5(a,b):
    l = []
    l.append(a)
    l.append(b)
    return max(l)

print(f"Maximum of two numbers version 1: {max_version_1(6,9)}")
print(f"Maximum of two numbers version 2: {max_version_2(6,9)}")
print(f"Maximum of two numbers version 3: {max_version_3(6,9)}")
print(f"Maximum of two numbers version 4: {max_version_4(6,9)}")
print(f"Maximum of two numbers version 5: {max_version_5(6,9)}")
