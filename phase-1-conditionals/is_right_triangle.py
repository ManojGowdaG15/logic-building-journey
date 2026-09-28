# Given three sides, check if a right-angled triangle can be formed

def valid_triangle(side1, side2, side3):
    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        return False
    elif (side1 + side2 <= side3) or (side1 + side3 <= side2) or (side2 + side3 <= side1):
        return False
    else:
        return True

def is_right_triangle(side1, side2, side3):
    valid = valid_triangle(side1, side2, side3)
    
    print("Triangle validity:", valid)
    
    # If the triangle is invalid, handle it first and exit early
    if not valid:
        print("Invalid Triangle (The given side lengths cannot form a triangle).")
        return
    
    if side1**2 + side2**2 == side3**2 or side1**2 + side3**2 == side2**2 or side2**2 + side3**2 == side1**2:
        print("The triangle is a right-angled triangle.")
    else:
        print("The triangle is not a right-angled triangle.")


side1 = int(input("Enter the length of side 1: "))
side2 = int(input("Enter the length of side 2: "))
side3 = int(input("Enter the length of side 3: "))

is_right_triangle(side1, side2, side3)
