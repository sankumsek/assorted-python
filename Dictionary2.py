#Dictionary Project 2

def gradebook():
    print ("1. Add")
    print ("2. Look up Grade")
    print ("3. Quit")


num = {}
menu = 0
gradebook()
while menu != 3:
    menu = eval(input("Type in either 1 or 2: "))
    if menu == 1:
        print("Add Name and Grade:")
        name = input("Name: ")
        grade = input("Grade: ")
        num[name] = grade
    elif menu == 2:
        print ("Lookup Person")
        name = input("Name: ")
        if name in num:
            print ("The grade is", num[name])
        else:
            print(name, "was not found")
    
        

































































































































        
