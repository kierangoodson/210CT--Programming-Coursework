def primeNumber():
    ''' A function that determines whether or not an input integer is a prime number or not'''
    prime = True
    if n >=2:                                           #Prime numbers begin at 2 and above.
        for i in range(2,n):                            #For every number between 2 and the input number

            if  (n % i) == 0:                           #Check if number is divisible with no remainder (if so, it's not prime)
                prime = False
    if n == 1:                                          #1 isn't considered a prime number.
        prime = False
        print (n, " is NOT a prime number because the definition of a prime number is any number that is greater than one that is only divisible by one and itself."
               "Since one is of course not greater than one, it does not fit the definition of a prime number.") 

    if prime == False:
        print(n," is NOT a prime number!")
    else:
        print(n," is a prime number!")


n = int(input("Input any number and this program will test if it is a prime number: "))

primeNumber()

