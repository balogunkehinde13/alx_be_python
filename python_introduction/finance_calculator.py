monthlyIncome = float(input("Enter your monthly income:"))
monthlyExpense = float(input("Enter your total monthly expenses:"))

monthlySavings = monthlyIncome - monthlyExpense

annualSavings = monthlySavings * 12

projectedSavings = annualSavings + (annualSavings * 0.05)

print(f"Your monthly savings are: ${monthlySavings}")
print(f"Projected savings after one year, with interest, is: ${projectedSavings}")