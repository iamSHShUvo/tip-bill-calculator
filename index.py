#Tip-bill-calculator

print("Welcome to the Tip Calculator!")

total_bill = float(input("What was the total bill?"))

tip = int(input("How much tip would you like to give? 10,15,20?"))

people = int(input("How many people to split the bill?"))

tip_as_percentage = tip/100

bill_with_tip = total_bill + tip_as_percentage

each_person_pays = total_bill/ people

# final_amount = round(each_person_pays, 2)

final_amount = "{:.2f}".format(each_person_pays)

print("Each person should pay : $", final_amount)

# print("Each person should pay: $")