#October 7, 2013 Notes
#Different techniques for manipulating/traversing a list


nums = [1,2,3,4]                                #how we've been doing it so far
for num in nums:
    print(nums)


for i in range(len(nums)):                      #new way
    print(i, nums[i])


def isAlphabetized(words):                      #function that tells you how if string is in alphabetical order
    for i in range(len(words) - 1):
        if words[i].lower > words[i+1].lower:
        
            return False
    return True

def space(word):
    result = []
    for i in range(len(word)):
        if word[i] == ' ':
            result.append(i)
    return result

def startSame1(words):                          #if all strings in list start with same letter
    for i in range(len(words)-1):
        if words[i][0] != words[i+1][0]:        #goes through each word and picks out the first character
            return False
    return True

    
def startSame2(words):
    target = words[0][0]
    for word in words:
        if word[0] != target:
            return False
    return True
