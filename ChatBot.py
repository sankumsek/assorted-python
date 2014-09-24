greeting = "Hello, I am your personal Butler Jeeves. What should I call you?"
import random
def chat(n):
    print(greeting)
    for i in range(n):
        print(reply(input("> ")))
    input("> ")
    print("Good day sir.")

def reply(sentence):
    sent1 = sentence.lower()
    sent = sent1.split()
    hello = ['boy', 'master', 'sir', 'junior', 'mister']
    fetch = ['coat','jacket','box','food','car']
    yes = ['yes','ya','yep']
    no = ['no','nope','naw']
    doublecheck = ['definitely','absolutely','for sure']
    for i in sent:
        if i in hello:
            return('How can I help you '+ i + '?')
        elif i in fetch:
            return("Let me go get " + i + " for you real quick...Ah here it is. Do you need anything else?")
        elif i in yes:
            return("Was that a " + i + " you just said? Well then, what else can I get you?")
        elif i in no:
            return("Was that a " + i + " you just said? Well, then it's off you go... Are you sure?")
        elif i in doublecheck:
            return(+ i + '? If you say so.')
    else:
        return("I can't understand you. Must be that horrible American accent of yours. Do you mind wording yourself differently?")
    return "Reply"
