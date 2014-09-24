#September 24, 2013 Notes

#grade tracker

grade = eval(input("numerical grade:"))

if grade >= 90:
    print("A")
elif 80 <= grade < 90:
    print("B")
elif 70 <= grade < 80:
    print("C")
elif 60 <= grade < 70:
    print("D")
elif grade < 60:
    print("F")

#'elif' assures mutual exclusion among all alternatives

def findDiscount(numItems):
    if numItems >= 2:
        return .10
    elif numItems >= 4:
        return .15
    elif numItems >= 6:
        return .20

#won't work properly because compiler will real the lines from top to bottom
#you must

#Basic Grammer analysis program
def WhatIsIt (word):
    if word[-3:] == 'ing':
        return 'gerund'
    elif word [-2:] == 'ly':
        return 'adverb'
    else:
        return 'no known classification'


def whereIsIt(word):
    if word.lower()[0] <= 'g':
        return 'start of alphabet'
    elif word.lower()[0] <= 'r':
        return 'middle of teh alphabet'
