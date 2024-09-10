# Assignment PE1 3.3 A - Logical Operations - Luke Kacprowicz

# Get input for two distinct integers
num1 = int(input("Enter an integer: "))
num2 = int(input("Enter another integer: "))

# Logical comparisons using the input integers
# and operator
result1 = num1 > 0 and num2 > 0
result2 = num1 > 100 and num2 > 100

# or operator
result3 = num1 % 2 == 0 or num2 % 2 == 0
result4 = num1 < 100 or num2 < 100

# not operator
result5 = not (num1 == num2)
result6 = not (num1 == 0)

# Print outcome results
print(f"Both numbers greater than 0: {result1}")
print(f"Both numbers greater than 100: {result2}")
print(f"Either number is even? {result3}")
print(f"Either number is less than 100? {result4}")
print(f"num1 is not equal to num2: {result5}")
print(f"num1 is not 0: {result6}")
