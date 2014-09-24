#October 8, 2013 Notes
def amountAfter(start,years,rate):
    for i in range(years):
        start = start * (1 + rate)
    return start

#limitation of for loop is definite iteration
#indefinite iteration requires 'while' loop

def doubleMyMoney(start,rate):
    current = start
    years = 0
    while current < start * 2:
        current = current * (1 + rate)
        years = years + 1
    return years

#routine hazard with while loops is infinite loop. Always try to use a for loop.


#using len action in while loop form
def length(s):
    count = 0
    while s != '':
        s = s[1:]
        count = count + 1
    return count


def outofMoney(start, expense):
    current = start
    years = 0
    while current >= expense:
        current = current - expense
        years = years + 1
    return years


def retirement(start, expense):
    current = start
    years = 0
    while current >= expense:
        prev = current
        current = current - expense
        current = current (1 + rate)
        if current >= prev:
            return "You will not run out of money"
        years = years + 1
    return years
    
    
