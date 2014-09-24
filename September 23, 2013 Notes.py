#September 23, 2013 Notes
def mysum(nums):
    total = 0
    for num in nums:
        total = total + num
        print ("total", total)
    return total
def rangeSum(start, end):
    total = 0
    for num in range(start, end + 1):
        total = total + num
    return total
def factorial(n):
    total = 1
    for num in range(1, n+1):
        total = total * num
    return total
def novowels(s):
    result = ''
    for char in s:
        if char.lower() not in 'aeiou':
            result = result + ch
    return result
def noGerunds(words):
    result = []
    for word in words:
        if word[-3:] != 'ing':
            result.append(word)
        return result
def longWords(words, n):
    result = []
    for word in words:
        if len(word) >= n:
            result.append(word)
        return result
    
    

    


