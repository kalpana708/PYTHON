# 1. Print all even numbers within a given range
start = int(input("Start of range: "))
end = int(input("End of range: "))

for num in range(start, end + 1):
    if num % 2 == 0:
        print(num, end=' ')
#2. Sum of all numbers from 1 to a given number
n = int(input("Enter a number: "))
total = sum(range(1, n + 1))
print("Sum:", total)
#3. Sum of all odd numbers within a given range
start = int(input("Start of range: "))
end = int(input("End of range: "))

total = 0
for num in range(start, end + 1):
    if num % 2 != 0:
        total += num
print("Sum of odd numbers:", total)
#4. Multiplication table of a given number
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
#5. Display numbers from a list using a for loop
numbers = [10, 20, 30, 40, 50]
for num in numbers:
    print(num)
#6. Count total number of digits in a number
num = input("Enter a number: ")
print("Number of digits:", len(num))
#7. Check if a string is a palindrome
s = input("Enter a string: ")
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
#8. Reverse a word input by user
word = input("Enter a word: ")
print("Reversed:", word[::-1])
#9. Check if a number is Armstrong
num = int(input("Enter a number: "))
order = len(str(num))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10
if num == sum:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
#10. Count number of even and odd numbers from a series
numbers = input("Enter numbers separated by spaces: ").split()

even = 0
odd = 0

for num in numbers:
    n = int(num)
    if n % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even numbers count:", even)
print("Odd numbers count:", odd)

#11. Display all numbers within a range except prime numbers
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

start = int(input("Start of range: "))
end = int(input("End of range: "))

for num in range(start, end + 1):
    if not is_prime(num):
        print(num, end=' ')
#12. Fibonacci series between 0 to 50
a, b = 0, 1
while a <= 50:
    print(a, end=' ')
    a, b = b, a + b
#13. Find factorial of a number
num = int(input("Enter a number: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print(f"Factorial of {num} is {fact}")
#14. Count digits and letters in a string
input_string = input("Enter a string: ")

letters = 0
digits = 0

for char in input_string:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1

print("Letters:", letters)
print("Digits:", digits)

#15. Iterate integers from 1 to 25
for i in range(1, 26):
    print(i, end=' ')
#16. Check validity of a password
import re

password = input("Enter password: ")

if (len(password) >= 8 and
    re.search("[a-z]", password) and
    re.search("[A-Z]", password) and
    re.search("[0-9]", password) and
    re.search("[@#$%^&+=]", password)):
    print("Valid password")
else:
    print("Invalid password")
#17. Convert month name to number of day
month_days = {
    "January": 31, "February": 28, "March": 31,
    "April": 30, "May": 31, "June": 30,
    "July": 31, "August": 31, "September": 30,
    "October": 31, "November": 30, "December": 31
}

month = input("Enter month name: ").capitalize()
days = month_days.get(month)

if days:
    print(f"{month} has {days} days.")
else:
    print("Invalid month name")
