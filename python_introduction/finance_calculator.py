monthlyIncome = int(input("Enter your monthly income:"))
monthlyExpense = int(input("Enter your total monthly expenses:"))

monthlySavings = monthlyIncome - monthlyExpense

projectedSavings = monthlySavings * 12 + (monthlySavings * 12 * 0.05)

print(f"Your monthly savings are: ${monthlySavings}")
print(f"Projected savings after one year, with interest, is: ${projectedSavings}")