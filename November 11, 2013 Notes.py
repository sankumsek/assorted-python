#November 11, 2013 Notes


lst = []
lst.append(5)
print.(lst.append(7))

lst2 = lst + [9]

#putting those two ideas together
lst = lst + [11]


#more efficient way (append1 is the faster way)

def append1(x):
    lst = []
    for i in range(n):
        lst.append(i)
    return lst

def append2(n):
    lst = []
    for i in range(n):
        lst = lst + [i]
    return lst

def timeTest(func, n):
    start = time.time()
    func(n)
    duration = time.time() - start
    return duration






