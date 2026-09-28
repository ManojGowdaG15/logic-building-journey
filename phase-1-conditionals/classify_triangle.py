# Classify a triangle (equilateral / isosceles / scalene / invalid)
def valid_triangle(side1, side2, side3):
    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        return False
    elif (side1 + side2 <= side3) or (side1 + side3 <= side2) or (side2 + side3 <= side1):
        return False
    else:
        return True

def classify_triangle(side1, side2, side3):
    valid = valid_triangle(side1, side2, side3)
    
    print("Triangle validity:", valid)
    
    # If the triangle is invalid, handle it first and exit early
    if not valid:
        print("Invalid Triangle (The given side lengths cannot form a triangle).")
        return

    # Now we safely classify because we know 'valid' is True
    if side1 == side2 == side3:
        print("The triangle is Equilateral.")
    elif side1 == side2 or side2 == side3 or side1 == side3:
        print("The triangle is Isosceles.")
    else:
        print("The triangle is Scalene.")
    

side1 = int(input("Enter the length of side 1: "))
side2 = int(input("Enter the length of side 2: "))
side3 = int(input("Enter the length of side 3: "))

classify_triangle(side1, side2, side3)
