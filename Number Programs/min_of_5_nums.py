def min_version_1(a,b,c,d,e):
    return min(a,b,c,d,e)

def min_version_2(a,b,c,d,e):
    return a if a<b and a<c and a<d and a<e else b if b<c and b<d and b<e else c if c<d and c<e else d if d<e else e

def min_version_3(a,b,c,d,e):
    if a < b and a < c and a < d and a < e:
        return a
    elif b < c and b < d and b < e:
        return b
    elif c < d and c < e:
        return c
    elif d < e:
        return d
    else:
        return e


def min_version_4(a,b,c,d,e):
    call = lambda  a,b,c,d,e: a if a<b and a<c and a<d and a<e else b if b<c and b<d and b<e else c if c<d and c<e else d if d<e else e
    return call(a,b,c,d,e)

def min_version_5(a,b,c,d,e):
    l = []
    l.append(a)
    l.append(b)
    l.append(c)
    l.append(e)
    l.append(d)
    return min(l)

print(f"Minimum of two numbers version 1: {min_version_1(6,9, 10, 12, 8)}")
print(f"Minimum of two numbers version 2: {min_version_2(6,9, 10, 12, 8)}")
print(f"Minimum of two numbers version 3: {min_version_3(6,9, 10, 12, 8)}")
print(f"Minimum of two numbers version 4: {min_version_4(6,9, 10, 12, 8)}")
print(f"Minimum of two numbers version 5: {min_version_5(6,9, 10, 12, 8)}")
