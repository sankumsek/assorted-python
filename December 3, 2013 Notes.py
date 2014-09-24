#December 3, 2013 Notes
#regular expression library

import re

s = "I need a cab. The cabbie charged too much."
re.findall("a", s)#requires two parameters: pattern and what your looking at
re.findall("[ab]", s)
re.findall("[abc]",s)
re.findall("[a-c]", s) #uses range of statement
re.findall("[a-z]+", s) #plus means one or more of them; does miss uppercase though
re.findall("[a-zA-Z]+", s)
re.findall("a-zA-Z.]+", s) # can use a backslash symbol sometimes
re.findall(".+", s)
s2 = 'I need a cab.\nThe cabbie charged too much.'
re.findall(".+", s2)
#doing with integers
re.findall("[0-9]", "12, 13, 54, 34")
re.findall("[0-9]", "12, 13, -54, 34") #ingores negative sign and gives positive integer
re.findall("-?[0-9]", "12, 13, -54, 34")
#finally phrase with 2 words (\s matches with backspace and tabs)
re.findall("[a-zA-Z]+\s[a-zA-Z]+", s)
#greedy property: once matched with two words doesn't use again

#writing as functions
import re
def findWords(s):
    return re.findall("[A-Za-z]+", s)

