#Chapter 6 Part 3

#6.21

def ticker(filename):
    result = {}
    infile = open(filename)
    text = infile.readlines()
    for line in range(len(text)):
        if line % 2 == 0:
            result[text[line].strip()] = text[line + 1].strip()
    name = (input("Enter Company Name: "))
    name = name.upper()
    while len(name) != 0:
        print ("Ticket Symbol: " + result[name])
        name = (input("Enter Company Name: "))
        name = name.upper()
    infile.close()


#6.23
def scarDict(filename):
    infile = open(filename)
    text = infile.read()
    for word in range (len(text)):
        if word in ['"',"'",'/','\n','\t',':',';','.',',','?','!','&']:
            text.remove(word)
    text.split()
    text.sort()
    outfile = open('dictionary.txt', 'w')
    for o in text:
        outfile.write(o)
        outfile.write('w')
    infile.close()
    outfile.close()
    
