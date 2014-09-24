#September 24, 2013 Assignment

#5.12
def test(nums):
    if nums > 0:
        return 'Positive'
    elif nums < 0:
        return 'Negative'
    else:
        return 'Zero'

#5.24
def case(word):
    if 'Z' >= word[0] >= 'A':
        return 'capitalized'
    elif 'z' >= word[0] >= 'a':
        return 'not capitalized'
    else:
        return 'unknown'

#5.25
def leap(year):
    if year%400 == 0:
        return 'True'
    elif year%100 == 0:
        return 'False'
    elif year%4 == 0:
        return 'True'
    else:
        return 'Unknown'

#5.25
def letter2number(grade):
    if grade == 'A+':
        return '4.3'
    elif grade == 'A':
        return '4.0'
    elif grade == 'A-':
        return '3.7'
    elif grade == 'B+':
        return '3.3'
    elif grade == 'B':
        return '3.0'
    elif grade == 'B-':
        return '2.7'
    elif grade == 'C+':
        return '2.3'
    elif grade == 'C':
        return '2.0'
    elif grade == 'C-':
        return '1.7'
    elif grade == 'D+':
        return '1.3'
    elif grade == 'D':
        return '1.0'
    elif grade == 'D-':
        return '0.7'
    elif grade == 'F':
        return '0'
    else:
        return 'Unknown'
