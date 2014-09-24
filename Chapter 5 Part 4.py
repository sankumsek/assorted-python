#Chapter 5 Part 4
#5.33
def mystery(n):
    repeat = 0
    while n != 1:
        n = n // 2
        repeat = repeat + 1
    return repeat


#5.38
def collatz(x):
    while x != 1:
        print(x)
        if x % 2 == 0:
            x = x // 2
        else:
            x = 3*x + 1
    return x
