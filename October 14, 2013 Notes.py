#October 14, 2013 Notes



#no parameters until user stops
#takes data from user and stores in a list
def payroll():
    result = []                                     #this is the empty list
    name = input("Enter Name: ")
    while name != '':                               #can also be stated as 'while len(name) > 0'
        pay = eval(input("Enter pay: "))
        result.append([name, pay])                 #adds into list
        name = input("Enter Name: ")                
    return result


def highestPaid(roll):
    highest = roll[0]
    for name, pay in roll:
        if pay > highest[1]:
            highest = [name, pay]
    print("Highest Paid Employee is", highest[0], "with pay", highest[1])


def lowestPaid(roll):
    lowest = roll[0]
    for name, pay in roll:
        if pay < lowest[1]:
            lowest = [name, pay]
    print("Lowest Paid Employee is", lowest[0], "with pay", lowest[1])


def toFile(roll, filename):
    outifle = open(filename, 'w')                   #opens file to write
    for name, pay in roll:
        outfile.write(name)
        outfile.write(' ')
        outfile.write(str(pay))
        outfile.write('/n')
    outfile.close()

def fromFile(filename):
    infile = open(filename, 'r')
    result = []
    for line in infile:
        name, pay = line.split()                    #because of the space in toFile, the split works
        result.append([name, pay])
    return result
