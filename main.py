#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

# round(150 / 5 * 1.12, 2)

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the Tip Calculator!")

#input("What percentage tip would you like to give? 10, 12, or 15?\n ")

bill = float(input("How much was the bill total?\n "))
tip = int(input("How much percentage tip would you lke to give?\n "))
people = int(input("How many people to split the bill?\n "))
bill_with_tip = tip / 100 * bill + bill

print(round(bill_with_tip / people, 2))
