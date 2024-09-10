#Assignment PE1 3.1 A: Making Decisions in Python - Luke Kacprowicz

# Use age as input
user_age = int(input("Please enter your age: "))

# Check if the person is old enough to drive
if user_age >= 16:
    print("You are old enough to drive.")
else:
    print("You are not old enough to drive.")

# Check if the person can vote
if user_age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")

# Check if the person can legally buy alcohol
if user_age >= 21:
    print("You can legally buy alcohol.")
else:
    print("You are not old enough to buy alcohol legally.")

# Check if the person is eligible for a senior discount (65 or older)
if user_age >= 65:
    print("You are eligible for a senior discount.")
else:
    print("You are not eligible for a senior discount.")
