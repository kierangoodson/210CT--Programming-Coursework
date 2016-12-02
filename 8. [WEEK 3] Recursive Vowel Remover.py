def vowelKiller():

    VOWELS = ("a","e","i","o","u")          #Vowels is a constant. Stored as list. This will never change.

    n = input("Input any word and this program will remove its vowels: ")

    new = ""                                #'new' variable used as spacing for output

    for letter in n:                        #for letter in input, if letter =! vowel, join new string and print
        if letter not in VOWELS:
            new = new + letter
    print (new)

vowelKiller()
