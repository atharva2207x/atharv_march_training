price = int(input("Enter the amount you have shopped for:"))
membership = str(input("are you a premium member:"))
while membership != "yes" and membership != "no":
    membership = str(input("Please enter yes or no:"))
while price < 0 or price > 100000:
    price = int(input("Please enter a valid amount:"))
    print("sorry you are not eligible for the discount")
if 2000 <= price <= 5000 and membership.lower() == "yes":
    print("you are eligible for a 10% discount")
    print(f"original price is {price}")
    print(f"your discounted price is {(price * 0.10)}")
    print(f"final price is {price - (price * 0.10)}")
if 2000 <= price <= 5000 and membership.lower() == "no":
    print("sorry you are not eligible for the discount")
    print(f"original price is {price}")
if 5000 < price <= 10000 and membership.lower() == "yes":
    print("you are eligible for a 15% discount")
    print(f"original price is {price}")
    print(f"your discounted price is {(price * 0.15)}")
    print(f"final price is {price - (price * 0.15)}")
if 5000 < price <= 10000 and membership.lower() == "no":
    print("sorry you are not eligible for the discount")
    print(f"original price is {price}")