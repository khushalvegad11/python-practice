# Data types

# String

# index strig

print("khushal"[3])
print('123'+'456')

# integer

print(123 + 456)

# flot

print(3.65647)

# Boolean

True
False

# type

name_char = len(input("what is your name ? "))
print(type(name_char))
kk = str(name_char)
print("your name has " + kk + " characters.")

# by using type check its which type is data type is it.

# math operaters

3 + 4
3 - 4
3 * 4
3 / 4
3 ** 4

Pemdaslr
()
**
*
/
+
-

print(3*3+3/3-3)
print(3*(3+3)/3-3)



# Round 
print(round(5 / 4))

print(round(5 / 4, 3))

# f string

score = 40
print(f"your score is {score}")


#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("welcome to the tip calculator.")

bill = float(input("what was the total bill ?"))
print(bill)

tip = int(input("how much tip would you like to give?10,12 or 15 ?"))

people = int(input("how many people to split the bill"))

percent = tip / 100
total_tip_amount = bill * percent
total_bill = bill + total_tip_amount
per_person = total_bill / people

final_amount = round(per_person, 2)
print(f"each person should pay: ${final_amount}")