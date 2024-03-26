import math

def divide_or_square(number):
    if number % 5 == 0:
        return f"The sqareroot of {number} is {math.sqrt(number)}"
    else:
        remainder = number % 5
        return f"The remainder of dividing {number} by 5 is {remainder}"
        
print(divide_or_square(10))
print(divide_or_square(8))