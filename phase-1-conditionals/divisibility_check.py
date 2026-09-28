# Check divisibility by 3, 5, or both (FizzBuzz)

number = int(input("Enter a number: "))

if number % 3 == 0 and number % 5 == 0:
    print(f"FizzBuzz: The number {number} is divisible by both 3 and 5.")
elif number % 3 == 0:
    print(f"Fizz: The number {number} is divisible by 3.")
elif number % 5 == 0:
    print(f"Buzz: The number {number} is divisible by 5.")
else:
    print(f"The number {number} is not divisible by 3 or 5.")