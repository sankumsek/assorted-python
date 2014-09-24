#Regular Expressions HW

#1
s = "3.1415, -2,71828, 4.0, 8.9, the value is 3.2, etc."
import re
def findfloats(s):
    return re.findall("-?[0-9]+[0.-9.]+",s)


#2
prices = open("print.txt").read()

def findPrices(prices):
    return re.findall("\$[0-9\.]+", prices)

#3

def findCapitalizedWords(s):
    return re.findall("[A-Z]+[a-z]+",s)

#4
def findSentences(s):
    return re.findall("[A-Z]+[A-Za-z\s\,\-]+[\.]",s)
