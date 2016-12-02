zeros= 0

fact = int(input("Input any whole, factorial number and this program will calculate the number of trailing zeros it has: "))

while fact != 0:                                 #While the factorial isn't equal to zero
    fact = fact/5                                #factorial = factorial divided by 5
    zeros = zeros + int(fact)                    #zeros becomes zero + factorial
print("The number of trailing zeros is : ",zeros)
