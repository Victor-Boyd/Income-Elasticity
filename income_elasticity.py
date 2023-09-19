import math

# Input values
quantity1 = 400
quantity2 = 450
income1 = 50000
income2 = 60000


# Calculating the midpoint of income and quantity
midpoint_quantity = (quantity1 + quantity2) / 2
midpoint_income = (income1 + income2) / 2

# Calculating percentage change in quantity demanded
quantity_percentage_change = ((quantity2 - quantity1) / midpoint_quantity) * 100

print("Percent change in quantity =", quantity_percentage_change, "%")

# Calculating percentage change in income
income_percentage_change = ((income2 - income1) / midpoint_income) * 100

print("Percent change in income =", income_percentage_change, "%")

# Calculating income elasticity
income_elasticity = quantity_percentage_change / income_percentage_change

# Print income elasticity
print("Income elasticity =", income_elasticity)

# Interpretation
if income_elasticity > 1:
    print("Income is highly elastic (normal good)")
elif income_elasticity > 0 and income_elasticity <= 1:
    print("Income is elastic (normal good)")
elif income_elasticity < 0:
    print("Income is inelastic (inferior good)")
elif income_elasticity == 0:
    print("Income has no effect on quantity demanded (perfectly inelastic)")
else:
    print("Income elasticity has another interpretation")
