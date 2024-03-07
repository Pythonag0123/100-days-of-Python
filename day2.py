#Day2-Project2
print("Welcome to the Tip Calculator")
total_bill=input("What was the total bill?").strip().replace("$",'')
number_of_people=int(input("Enter the number of people:").strip())
total_bill=float(total_bill)
tip_cent=input("What percentage of the bill you want to pay as tip?").replace("%",'').strip()
tip_cent=float(tip_cent)
tip_per_person=((tip_cent/100)*total_bill)/number_of_people
print("each person has to pay" + str(tip_per_person))

