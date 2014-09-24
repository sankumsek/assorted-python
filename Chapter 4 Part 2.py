#Chapter 4 Part 2 Assignment
#4.26
def printFile(filename):
    infile = open(filename)
    text = infile.read()
    infile.close()
    switch = text.replace('secret','xxxxxx')
    print(switch)
    
#4.29
def stats(filename):
    infile = open(filename)
    text = infile.read()
    infile.close()
    line = text.count('\n')
    word = len(text.split())
    char = len(text)
    
    print("Line count:" + str(line))
    print("Word count:" + str(word))
    print("Character count:" + str(char))


    
