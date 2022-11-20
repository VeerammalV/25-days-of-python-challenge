#to get a prime number between given interval

lowernumber = int(input("Enter an integer:"))
uppernumber = int(input("Enter an integer:"))

print("The prime number between ", lowernumber, "and", uppernumber, "are:")
for num in range(lowernumber, uppernumber +1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)
            
#OUTPUT
Enter an integer:34
Enter an integer:97
The prime number between  34 and 97 are:
37
41
43
47
53
59
61
67
71
73
79
83
89
97            
            