#After Test 3

#1
def reverse(list):
    length = len(list)
    i = length
    new_list = [None]*length

    for item in list:
        i = i - 1
        new_list = item
    return new_list
