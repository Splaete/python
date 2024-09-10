# Assignment PE1 3.2 B - For Loops in Python - Luke Kacprowicz

# Check the range of numbers from 1 to 300. (This is set to 301 not 300 because we want to include the number 300 in our range)
for number in range(1, 301):
    # Inside the loop, use an if statement to check if a number is divisible by 7.
    if number % 7 == 0:
        # If a number is divisible by 7, print that number.
        print(number)
