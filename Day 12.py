#simple interest calculator

def simpleInterest(P,n,r):

    return(P*n*r/100)

principal = int(input("Enter the principal value:"))
year = int(input("Enter the year:"))
rate = int(input("Enter the rate:"))

interest = simpleInterest(principal,year,rate)
print("The Simple interest is ",interest)


#OUTPUT
Enter the principal value:300000
Enter the year:10
Enter the rate:30
The Simple interest is  900000.0