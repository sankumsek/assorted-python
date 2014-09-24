#October 10, 2013 Notes

#write a function to estimate a value of e.
def eTerm(term):
    denom = 1
    for i in range(1 ,term+1):
        denom = denom *i
    return 1.0/denom

def approxE(error):                     #limit on how bad error could be
    prev = eTerm(0)
    approx = prev + eTerm(1)
    i = 2
    while abs(prev-approx) > error:
        prev = approx
        approx = approx + eTerm(i)
        i = i + 1
    return approx
    
