print("Welcome to the bonus calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage bonus would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
percentage_of_bill = bill * tip / 100
total = bill + percentage_of_bill
print(f"Each person should pay ${round(total/people, 2)}.")
