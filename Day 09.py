#To check whether the given number is armstrong or not

number = int(input("Enter an integer: "))

#initializing sum
sum = 0

#to find the sum of the each digit
temp = number
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //=10

if (number == sum):
    print(number, " is an Armstrong number")

else:
    print(number, " is not an Armstrong number")
    

#OUTPUT
Enter an integer: 378
378  is not an Armstrong number

Enter an integer: 407
407  is an Armstrong number