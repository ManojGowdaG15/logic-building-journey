# Given marks, print the grade using a grading scale
try:
    marks = float(input("Enter the marks (Out of 100): "))

    # Validate if the entered marks are within the realistic 0-100 range
    if marks < 0 or marks > 100:
        print("Invalid input! Marks must be between 0 and 100.")
    else:
        # Since it's out of 100, 'marks' is already the percentage value
        if marks >= 91:
            print("Your Grade is O -- Outstanding")
        elif marks >= 81:
            print("Your Grade is A+ -- Excellent")
        elif marks >= 71:
            print("Your Grade is A -- Very Good")
        elif marks >= 61:
            print("Your Grade is B -- Good")
        elif marks >= 51:
            print("Your Grade is C+ -- Above Average")
        elif marks >= 41:
            print("Your Grade is C -- Average")
        elif marks >= 35:
            print("Your Grade is D -- Pass")
        else:
            print("Your Grade is E -- Fail")
            
except ValueError:
    print("Please enter a valid numeric value.")
