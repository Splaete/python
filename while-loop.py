# Assignment PE1 3.2 A - While Statements in Python - Luke Kacprowicz

# Give the variable 'bottles' with the starting value of 99
bottles = 99
# Start a while loop that continues as long as there are bottles left
while bottles > 0:
    # Check if there is more than one bottle to adjust the wording and remove a bottle
    if bottles > 1:
        print(f"{bottles} bottles of beer on the wall")
        print(f"{bottles} bottles of beer")
        print("Take one down, pass it around")
        bottles -= 1
        if bottles == 1:
            print(f"{bottles} bottle of beer on the wall!\n")
        else:
            print(f"{bottles} bottles of beer on the wall!\n")
            # When none left print the statement
    else:
        print(f"{bottles} bottle of beer on the wall")
        print(f"{bottles} bottle of beer")
        print("Take it down, pass it around")
        bottles -= 1
        print("No bottles of beer on the wall!\n")
