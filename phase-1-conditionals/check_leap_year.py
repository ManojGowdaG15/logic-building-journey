# Check whether a year is a leap year

year = int(input("Enter the Year: "))

if year > 0:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
else:
    print("Enter positive year only.")