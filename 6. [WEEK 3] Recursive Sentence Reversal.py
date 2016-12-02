def sentenceReversal (string, reverse):
    '''A function that reverses any given sentence. '''
    if len(string) == 0:                                    #If length of string is 0...
        return reverse                                      #Return reverse (this will not output anything if nothing is input in the first place)
    else:
        reverse = reverse + " " + string.pop()              #Takes first word off array and puts it as first word in sentence                               
        return sentenceReversal(string,reverse)


sent = input("Input a sentence and this program will reverse it: ")

List = sent.split()                                                         #.split creates a list of every word in the input string.
reverse = "Your sentence reversed looks like this: "

print(sentenceReversal(List, reverse))
