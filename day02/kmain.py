
print("Welcome to the tip calculator!")
billamount = float(input("What is the total bill amount? "))
tipamount = int(input("How much tip would you like to give in percent? "))
splitppl = int(input("How many people to split the bill with? "))

billtip = billamount * ((tipamount/100)+1)
gesamt = billtip / splitppl

print(f"Each person should pay: {gesamt:.2f} €")