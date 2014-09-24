#Chapter 5 Part 5 Assignment

#5.40
def Pie(term):
    denom = ((term+1)*2 - 1)
    return 4.0 / denom

def approxPi(error):
    prev =  Pie(0)
    approx = prev - Pie(1)
    x = 2
    add = True
    while abs(prev - approx) > error:
        prev = approx
        if add == True:
            approx = approx - Pie(x)
            add = False
        else:
            approx = approx + Pie(x)
            add = True
        x = x + 1
    return approx
#5.49
def heron(n, error):
    prev = 1.0
    approx = 0.5*(prev + n/prev)
    while abs(prev - approx) > error:
        prev = approx
        approx = 0.5*(prev + n/prev)
    return approx
