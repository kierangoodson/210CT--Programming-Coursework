def shuffleArray():
    '''A function that randomly shuffles an array. The function takes a random element from
the array and swaps it's position with the element in index 0. It does this for every number in
the array.'''

    array = [1,2,3,4,5,6,7,8]
    print("The original array: ",array)
    import random
    for i in array:
        randInt = random.randrange(0, len(array))               #randomly selects element in array
        array[0], array[randInt] = array[randInt], array[0]     #swap element at index 0 with the randomly selected element. 
    print ("The randomly shuffled array: ",array)

shuffleArray()

