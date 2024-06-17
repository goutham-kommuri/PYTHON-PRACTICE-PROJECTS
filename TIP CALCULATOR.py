# Welcome message
print("Welcome to the Tip Calculator!")

# Get the total bill amount
total_bill = float(input("What was the total bill? $"))

# Get the tip percentage
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

# Get the number of people splitting the bill
number_of_people = int(input("How many people to split the bill? "))

# Calculate the tip amount
tip_amount = total_bill * (tip_percentage / 100)

# Calculate the total amount to be paid
total_amount = total_bill + tip_amount

# Calculate the amount each person needs to pay
amount_per_person = total_amount / number_of_people

# Format the result to 2 decimal places
amount_per_person = "{:.2f}".format(amount_per_person)

# Print the results
print(f"Each person should pay: ${amount_per_person}")
