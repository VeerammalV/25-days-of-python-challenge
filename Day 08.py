# to find the factorial pf the given number

number = 24

factorial  = 1

if (number < 0):
    print("The factorial doesn't exists")

elif (number == 0):
    print("The factorial of 0 is 1")

else:
    for i in range(1, number + 1):
        factorial = factorial * i
    print("The factorial of ",number, "is ", factorial)    