
def highestPerfectSquare():
    ''' A function that finds the highest perfect square that is less than or equal to
    any given integer input'''
    squareRoot = (n)**0.5                               #to find square root of number = number to the power of 0.5.
    perfectSquare = (int(squareRoot))**2                #perfect square is square root to the power of 2. 

    print("\n", perfectSquare, " is the nearest perfect square that is <=", n)

n = int(input("Input a positive integer and this program will output the highest perfect square that is <= to it: "))

highestPerfectSquare()
