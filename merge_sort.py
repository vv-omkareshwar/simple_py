def f(a):
    if len(a) <= 1:
        return a
    m = len(a) // 2
    b = f(a[:m])
    c = f(a[m:])
    return g(b, c)

def g(b, c):
    d = []
    i = j = 0
    while i < len(b) and j < len(c):
        if b[i] < c[j]:
            d.append(b[i])
            i += 1
        else:
            d.append(c[j])
            j += 1
    d.extend(b[i:])
    d.extend(c[j:])
    return d

x = [5, 2, 9, 1, 7, 3, 8]
print(f(x))
