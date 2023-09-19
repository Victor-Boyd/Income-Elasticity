import math

# make sure not to forget to put a negative sign for decreases!

# Input values
quantity_percentage_change = -0.05
income_percentage_change = -.13

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