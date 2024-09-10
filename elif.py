# Assignment PE1 3.1 B: elif - Luke Kacprowicz
# Get student's grade
grade = int(input("What is your current grade?  "))
# Check if grade is between 0 and 100
if 0 <= grade <= 100:
    # Convert number grade to letter grade
    if grade >= 90:
        letter = 'A'
    elif grade >= 80:
        letter = 'B'
    elif grade >= 70:
        letter = 'C'
    elif grade >= 60:
        letter = 'D'
    else:
        letter = 'F'

    print("Your letter grade is:", letter)
else:
    print("Nice try! Please enter a grade between 0 and 100.")
