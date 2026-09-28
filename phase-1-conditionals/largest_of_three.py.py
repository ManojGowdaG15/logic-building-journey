# Find the largest of three numbers without using max()

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))

if num1 > num2 and num1 > num3:
    print(f"The largest number is {num1}.")
elif num2 > num1 and num2 > num3:
    print(f"The largest number is {num2}.")
else:
    print(f"The largest number is {num3}.")