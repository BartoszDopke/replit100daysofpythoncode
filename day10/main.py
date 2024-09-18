bill = float(input("What was the bill?: "))
tip = int(input("What % of tip you will leave to be added to the bill total? "))
total_bill = bill + tip/bill
number_of_people = int(input("How many people?: "))
answer = total_bill / number_of_people
print("You all owe", answer)