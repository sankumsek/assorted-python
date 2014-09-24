#Project: Files


#1: Paycheck on timecard
def payroll():
    result = []
    name = input("Enter Name: ")
    while name != '':
        hours = eval(input("Enter Hours Worked: "))
        wage = eval(input("Enter Hourly Wage: "))
        pay = hours * wage
        result. append([name, hours, wage, pay])
        name = input("Enter Name: ")
    return result

def highestPaid(roster):
    highest = roster[0]
    for name, hours, wage, pay in roster:
        if pay > highest[1]:
            highest = [name, hours, wage, pay]
    print("Richest Worker is", highest[0], "working for", highest [1], "hours with a hourly wage of", highest[2], " with a total pay of", highest[3], "dollars." )        

def intoFile(roster, filename):
    outfile = open(filename, 'w')
    for name, pay in roster:
        outfile.write(name)
        outfile.write(' ')
        outfile.write(str(pay))
        outfile.write('/n')
    outfile.close()

def outofFile(filename):
    infile = open(filename, 'r')
    result = []
    for line in infile:
        name, pay = line.split()
        result.append([name, pay])
        
