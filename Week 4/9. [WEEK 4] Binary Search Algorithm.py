myList = []
print("This program will ask you six times to enter an integer.")
print("Please input these integers in ASCENDING order...")
for i in range(0,6,1):                                                                   #Asks user 6 times for integer.                                        
        number = int(input("Please input an integer: "))
        myList.append(number)                                                            #Appends input numbers to list, myList
print ("Your sequence is = ", myList)

lower = int(input("Please input an integer for the lower bound: "))                     #Getting the users upper and lower bounds
upper= int(input("Please input another larger integer for the upper bound: "))

if upper < lower:
        print("You have entered a lower number than the last")
elif upper == lower:
        print("You have entered the same number twice")

def binarySearch(myList, lower, upper):
    '''A function that uses the binary search algorithm to determine
        if an input list of integers is within two input lower and upper bounds.
        The binary algorithm splits the list into 2 parts with a midpoint and compares the bounds
        to it. It then does the logical comparisons to check whether there are numbers in the
        list that are within those bounds.'''
    
    if len(myList) == 1:                                                                  #if the length of list = 1, middle = list index 0. Otherwise, middle = length of list/2.
        mid = myList[0]
    else:                                                                                #Otherwise... lowest is list index 0nd mid is 
        lowest = myList[0]                                                               #lowest is list index 0
        highest = len(myList)-1                                                          #highest is list index length-1 (the last element)
        mid = int((len(myList))/2)                                                       #mid = length of list/2
        
        
    length = len(myList)
        
    if upper < myList[0] or lower > myList[length-1]:                                    #If upper bound is less than List index 0 or lower bound is greater than last item in list...
        print("There is no number between", lower, "and", upper)
        return
                                                                              #User interval is outside list so there is no number between the lower and upper.
    print(lower, upper, mid)
    
    if lower <= myList[mid] and upper >= myList[mid]:                                         #If lower is less than middle of the list
                
        for i in range (lower, upper):                                                #Iterates over the interval to see if there is a number in the array
             if i in myList:                                                          #If so, there is a number!
                  print("There is a number between",lower, "and", upper)
                  return False


    elif lower < myList[mid] and upper < myList[mid]:           #If lower and upper bounds are both less than midpoint of list, only operate on the first half of the list.
        return binarySearch(myList[0:mid], lower, upper)

    elif lower > myList[mid] and upper > myList[mid]:           #If lower and upper bounds are both higher than midpoint of list, only operate on the second half of the list.
        return binarySearch(myList[mid:], lower, upper)
    
    else:
        return

binarySearch(myList, lower, upper)
