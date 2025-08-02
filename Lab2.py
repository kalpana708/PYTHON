# 1. Check if a year is a leap year or not
print("\n1. Leap Year Check")
year = int(input("Enter a year: "))
# A year is a leap year if:
# it is divisible by 4 and not divisible by 100, or divisible by 400
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a Leap Year.")
else:
    print(f"{year} is Not a Leap Year.")
# 2. Find the largest among three numbers
print("\n2. Find the Largest of Three Numbers")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b and a >= c:
    print("The largest number is:", a)
elif b >= a and b >= c:
    print("The largest number is:", b)
else:
    print("The largest number is:", c)
# 3. Check if a number is positive, negative or zero
print("\n3. Check if Number is Positive, Negative or Zero")
num = float(input("Enter a number: "))

if num > 0:
    print("The number is Positive.")
elif num < 0:
    print("The number is Negative.")
else:
    print("The number is Zero.")
# 4. Toy Vendor Discount Calculator
print("\n4. Toy Vendor Discount Calculator")
print("Toy Types:")
print("1 = Battery Based Toy")
print("2 = Key-based Toy")
print("3 = Electrical Charging Toy")

code = int(input("Enter Toy Product Code (1/2/3): "))
amount = float(input("Enter order amount (in ₹): "))

discount = 0  # Initial discount

if code == 1:  # Battery based toy
    if amount > 1000:
        discount = 0.10 * amount
elif code == 2:  # Key-based toy
    if amount > 100:
        discount = 0.05 * amount
elif code == 3:  # Electrical charging toy
    if amount > 500:
        discount = 0.10 * amount
else:
    print("Invalid product code!")

net_amount = amount - discount
print("Discount Applied: ₹", discount)
print("Net Amount to Pay: ₹", net_amount)
# 5. Transport Fare Calculator
print("\n5. Transport Company Fare Calculator")
distance = float(input("Enter Distance in Km: "))

# Charges per km based on distance range
if distance <= 50:
    fare = 8 * distance
elif distance <= 100:
    fare = 10 * distance
else:
    fare = 12 * distance

print(f"Total Fare to Pay: ₹{fare}")