# Objective:
# Students will use logical (and, or, not) and chained comparison operators in Python to build compound conditions.

# Key Notes:

# and → Both conditions must be True

# or → At least one condition must be True

# not → Inverts True/False

# You can chain comparisons: 1 < x < 5

# Examples:
x = 10
print(x > 5 and x < 15)   # True
print(x < 5 or x == 10)   # True
print(not(x == 10))       # False
print(1 < x < 20)         # True


# Practice Problems:

#GRADE CALCULATOR
#If the score is between 90 and 100 inclusive, print "A"
#If the score is between 80 and 89 inclusive, print "B"
#If the score is between 70 and 79 inclusive, print "C"
#If the score is between 60 and 69 inclusive, print "D"
grade = int(input("Enter your grade: "))
if (grade <= 100) and (grade >= 90):
    print(" Grade = A")
elif (grade <= 89) and (grade >= 80):
    print("Grade = B")
elif (grade <= 79) and (grade >= 70):
    print("Grade: C")
elif (grade <= 69) and (grade >= 60):
    print("Grade = D")
else:
    print("Grade is invalid.")

# Write an expression that checks if a number is between 50 and 100 (inclusive).

# Write an expression that checks if a number is NOT equal to 0 and greater than 10.

# Use chained comparison to check if 3 < 4 < 5.

# Challenge: Create a password rule using logical operators:

