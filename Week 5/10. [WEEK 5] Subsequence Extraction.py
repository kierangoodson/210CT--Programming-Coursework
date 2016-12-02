def getSequence():
    '''This function takes an input sequence of integers ONLY. '''
    
    seq = []                                                                                        
    loop = False
    print("This program will find the largest subsequence of any sequence you enter.")
    print("When you're finished entering, input anything other than an integer.")
    while loop == False:
        try:
            n = int(input("Please enter an integer into your sequence: "))
            seq.append(n)                                  #Appending input values to an empty list, seq.

        except ValueError:                                 #Raises value error if integer not input.
            loop = True
            return seq

def subSeqExtract(List):
    '''This function extracts subsequences from the original sequence
that are in ascending order. It uses an empty placeholder list to temporarily
store these subsequences before appending them to a list of lists '''
    listOfLists = []
    placeholder = []
    if len(List) == 0:
        return List
    else:
        for i in range (0,len(List)):

            if i == len(List)-1:                            #If on last item in list...
                placeholder.append(List[i])                 #Append items to placeholder list
                listOfLists.append(placeholder)             #Append placeholder list to list of lists 
                return listOfLists
            else:
                if List[i] <= List [i+1]:                   #Comparing if i <= to next item in list.
                    placeholder.append(List[i])             #Add to end of list.

                else:                                       #Otherwise...
                    placeholder.append(List[i])             #Next item is appended to placeholder list
                    listOfLists.append(placeholder)         #Append placeholder list to list of lists 
                    placeholder = []                        #Resetting the placeholder list as empty.

def compareSeqs(List):
'''This function compares each subsequence in the list of lists to find out
which is the largest. Then, outputs the largest one.'''
    largestSub = len([])                                    #The length of the list 
    index = []                                              #Creating list that keeps track of the largest list. 
    for i in range (0,len(List)):                           #For all lists in the entire list of lists...
        if len(List[i]) == largestSub:                      #If two subsequences are the same size...
            index.append(List[i])                           #Append to index.

        elif len(List[i]) > largestSub:                     #If subsequence is larger than the current largest subsequence...
            largestSub = len(List[i])                       #Updates largestSub. 
            if index != []:                                 #If index is not empty, empty it. 
                index = []
                index.append(List[i])                       #Append subsequence to index
            else:
                index.append(List[i])

    print(index)
    return

seq = getSequence()
compareSeqs(subSeqExtract(seq))
