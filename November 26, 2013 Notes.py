#November 26, 2013
#technique for writing shorter code in python

#list comprehension technique
#consider following

def double1(nums):
    result = []
    for num in nums:
        result.append(num * 2)
    return result

#better way to do it
def double2(nums):
    return [num * 2 for num in nums] #in list comprehension put action first

#more examples

def negate(nums):
    return [num * -1 for num in nums] #turns numbers negative


#another way of using list comprehension

def shortwords1(word, maxLength):
    result = []
    for word in words:
        if len(word) <= maxLength:
               result.append(word)
        return result
