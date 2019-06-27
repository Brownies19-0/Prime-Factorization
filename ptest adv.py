#prime factorization code

def pfact(y):
    facts = factors(y)[1:-1]
    s = " * "
    for i in facts:
        y = y / i
    if y == 1:
        y = [str(i) for i in facts]    
        return s.join(y)
    while y > 1:
        for i in factors(y)[1:-1]:
            if i != 1:
                facts += [i]
            y = y / i
    y = [str(i) for i in facts]
    return s.join(y)

def factors(y):
    a = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    c = [1]
    mod = list(ptest(y))
    for i in range(len(a)):
        if mod[i] == 0:
            c += [a[i]]
    c += [y]
    return c
    

def ptest(x):
    a = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    b = []
    for i in a:
        b += [x % i]
    return b

