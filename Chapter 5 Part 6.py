#Chapter 5 Part 6


#1
def basketballRoll():
    result = []
    name = input("Enter Name: ")
    while name != '':
        points = eval(input("Enter points: "))
        assists = eval(input("Enter assists: "))
        result.append([name, points, assists])
        name = input("Enter Name: ")
    return result

#2
def basketballStats(roll):
    highestpoints = roll[0]
    highestassists = roll[0]
    for name, points, assists in roll:
        if points > highestpoints[1]:
            highestpoints = [name, points, assists]
        if assists > highestassists[1]:
            highestassists = [name, points, asists]
    print ("Highest scoring player is", highestpoints, "and the highest passing player is", highestassists)
        
