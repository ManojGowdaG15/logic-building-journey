# Python Program to Check if a Number is Positive, Negative or 0
num = int(input("Enter a number: "))

if num >= 0:
    if num == 0:
        print(f"The number {num} is zero.")
    else:
        print(f"The number {num} is positive.")
else:
    print(f"The number {num} is negative.")