cash_price = float(input("Enter cash price:"))
points = float(input("Enter points required:"))
taxes = float(input("Enter taxes:"))
cpp = ((cash_price - taxes)/points)*100
print(f"Cents per point: {cpp:.2f}")
