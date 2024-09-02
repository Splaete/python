
# Asks the guest for the total budget
total_budget = float(input("Enter your total budget: "))

# Asks the guest for the amounts spent in each category
housing = float(input("Enter the amount spent on Housing (rent or mortgage): "))
utilities = float(input("Enter the amount spent on Utilities: "))
groceries = float(input("Enter the amount spent on Groceries: "))
transportation = float(input("Enter the amount spent on Transportation: "))
health_care = float(input("Enter the amount spent on Health Care: "))
personal_care = float(input("Enter the amount spent on Personal Care: "))
clothing = float(input("Enter the amount spent on Clothing: "))
debt = float(input("Enter the amount spent on Debt: "))

# Calculates the percentage of the total budget spent in each category
def calculate_percentage(amount, total):
    return (amount / total) * 100

housing = calculate_percentage(housing, total_budget)
utilities = calculate_percentage(utilities, total_budget)
groceries = calculate_percentage(groceries, total_budget)
transportation = calculate_percentage(transportation, total_budget)
health_care = calculate_percentage(health_care, total_budget)
personal_care_ = calculate_percentage(personal_care, total_budget)
clothing = calculate_percentage(clothing, total_budget)
debt = calculate_percentage(debt, total_budget)

# Shows the budget breakdown
print("\n--- Budget Breakdown ---")
print(f"Housing: {housing:.2f}% of total budget")
print(f"Utilities: {utilities:.2f}% of total budget")
print(f"Groceries: {groceries:.2f}% of total budget")
print(f"Transportation: {transportation:.2f}% of total budget")
print(f"Health Care: {health_care:.2f}% of total budget")
print(f"Personal Care: {personal_care:.2f}% of total budget")
print(f"Clothing: {clothing:.2f}% of total budget")
print(f"Debt: {debt:.2f}% of total budget")
