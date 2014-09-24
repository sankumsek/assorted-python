#Dictionary Project Part 1

translator = {"red": "rojo",
              "green": "verde",
              "fox": "zorro",
              "the": "el",
              "moon": "luna",
              "sun": "sol",
              "jumps": "salta",
              "up": "arriba",
              "crazy": "loco",
              "man": "hombre",
              "is": "es",
              "that": "este"}




while True:
    x = str(input("Welcome to your English to Spanish Translator: "))
    if x in translator:
        print ("And the the translation is:", translator[x],)
    else:
        print ("That word isn't in our dictionary. Sorry")
