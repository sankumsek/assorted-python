#Chapter 5 Part 8

#5.34
def statements(money):
    action = 0
    withdrawal = 0
    for i in money:
        if i > 0:
            action = action + i
        else:
            withdrawal = withdrawal + i
    billing = [action, withdrawal]
    return billing


#5.36
def prime(number):
    for num in range(2, number):
        if number % num != 1:
            return False
        else:
            return True


#5.39
def exclamation(word):
    empty = ''
    for letter in word:
        if letter in 'aeiouAEIOUyY':
            empty = empty + letter*4
        else:
            empty = empty + letter
    empty = empty + ''
    return empty

#5.44
def cipher(key, n):
    empty = ''
    for num in str(n):
        empty = empty + str(key)[eval(num)-1]
    return empty

#5.48

def sublist(list1, list2):
    for i in list1:
        if list1 in list2:
            return True
        else:
            return False
