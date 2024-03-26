def my_discount():
    price = int(input("Enter the price here: "))
    discount = float(input("Enter the discount here: "))
    discount_price = price - (price * discount)
    return f"The discounted price is ${discount_price}"

my_discount()