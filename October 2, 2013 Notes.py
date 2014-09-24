#October 2, 2013 Notes

#opens file and prints out contents

def printFile(filename):
    infile = open(filename)                 #file handle
    text = infile.read()                    #takes entire content of file and put it in string
    infile.close()                          #done with file.
    print(text)                             #prints content file
    


def printfileLines(filename):               #prints certain lines of file
    infile = open(filename)                 #to be more specific, use full path name
    for line in infile:
        print("line:",zapSlashN(line))                 #will print



def zapSlashN(string):
    if string[-1] == '/n':                  #removes extra spaces between line
        return string[:-1]
    else:
        return string


def printLineList(filename):
    infile = open(filename)                 #prints out as list of strings
    lines.infile.readlines()
    infile.close()
    print(lines)
