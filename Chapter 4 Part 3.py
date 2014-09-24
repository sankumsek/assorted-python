#Chapter 4 Part 3

#4.27
def fcopy(filename1,filename2):
    infile = open(filename1).read()
    outfile = open(filename2, 'w')
    outfile.write(infile)



#4.31
def duplicate(filename):
    infile = open(filename).read
    lst = infile.split()
    for name in filename:
        if name in lst:
            lst.remove(word)
            if word in lst:
                return True
        return False
            



#4.32
def censor(filename):
    infile = open(filename)
    text = infile.read()
    infile.close()
    for name in filename:
        if len(name) == 4:
            text = text.replace(name,xxxx)
    outfile.write(text)
 

        
    
    
