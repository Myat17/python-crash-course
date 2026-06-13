# Extra Exercise (Tip Calculator)
bill_amount = float(input("Enter the amount of bill: "))
tip_percentage = float(input("Enter tip percentage: "))

tip_amount = round(bill_amount * (tip_percentage / 100), 2)
total_amount = round(bill_amount + tip_amount, 2)

print(f"Bill amount: {bill_amount:.2f} USD.")
print(f"Tipping amount: {tip_amount:.2f} USD,")
print(f"The total billing amount is {total_amount:.2f} USD.")