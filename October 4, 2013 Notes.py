#October 4, 2013 Notes

#How to do a file output

def createFile(filename, numLines):
    outfile = open(filename, 'w')               #the 'w' means to write, 'r' means to read (does by default)
    for i in range(numLines):
        line = input("> ")
        outfile.write(line)                     #.write is a method that takes string and sends it to file; adds on to file
        outfile.write('/n')                     #appends the initial statement
    outfile.close()

#exception to calling 'return' function early
#correct function
def hasZero(nums):
    for num in nums:
        if num == 0:            
            return True                         
    return False

#incorrect function
def hasZero(nums):
    for num in nums:
        if num == 0:
            return true
        else:
            return False                        #Doesn't work because it won't read the rest of the string



#Another example of correct functions
def allPositive(nums):
    for num in nums:
        if num <= 0:
            return False
    return True

