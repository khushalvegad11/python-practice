# if / else

print("welcome to the rollercoaster !")

height = int(input("what is your hight in cm ?"))

if height >= 120 :
    
    print("you can ride the rollercoaster")
else:
    print("sorry , you can't ride the rollercoaster. ")

# >
# <
# >=
# <=
# ==
# !=

# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if number % 2 == 0:
    print("This is an even number.")
else :
    print("This is an odd number.")


# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi =round( height / weight ** 2)


if bmi < 18.5 :
    print(f"your bmi is {bmi} you are underweight")
elif bmi < 25 :
    print(f"your bmi is {bmi} you are normal weight")
elif bmi < 30 :
    print(f"your bmi is {bmi} you are slightly overweight")
elif bmi < 35 :
    print(f"your bmi is {bmi} you are obese")
else :
    print(f"your bmi is {bmi} you are clinically obese")
    
    
# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if year % 4 == 0:
    if year % 100 == 0 :
        if year % 400 == 0:
            print("leap year")
        else:
            print("not leap year")
    else:
        print("leap year")
else:
    print("not leap year")
    
    


print("welcome to the rollercoaster !")

height = int(input("what is your hight in cm ?"))
bill = 0

if height >= 120 :
    
    print("you can ride the rollercoaster")
    age = int(input("what is your age ?"))
    
    if age <= 12 :
        bill = 10
        print("pay 10$")
    elif age <= 18 :
        bill = 20
        print("pay 20$")
    else :
        bill = 30
        print("pay 30$")
        
        photo = input("do you want photo ? y or n :")
        if photo == "y":
            bill += 3
            print(f"your final bill {bill}")
    
else:
    print("sorry , you can't ride the rollercoaster. ")

# logical operator

# and
# not
# or

    print("welcome to the rollercoaster !")

    height = int(input("what is your hight in cm ?"))
    bill = 0

    if height >= 120 :
        
        print("you can ride the rollercoaster")
        age = int(input("what is your age ?"))
        
        if age <= 12 :
            bill = 10
            print("pay 10$")
        elif age <= 18 :
            bill = 20
            print("pay 20$")
        elif age >= 45 and age <=55 :
            print("free")
        else :
            bill = 30
            print("pay 30$")
            
            photo = input("do you want photo ? y or n :")
            if photo == "y":
                bill += 3
                print(f"your final bill {bill}")
        
    else:
        print("sorry , you can't ride the rollercoaster. ")
        
        
# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bill = 0

if size == "s":
    bill = 15
elif size == "m":
    bill = 20
else:
    bill = 25

if add_pepperoni =="y":
    if size == "s":
        bill += 2
    else:
        bill += 3

if extra_cheese =="y":
    bill += 1

print(f"your final bill is {bill}")


# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combind_string = name1 + name2
lower_case_string = combind_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

love_score = str(true) + str(love)

if (love_score < 10) or (love_score > 90) :
    print(f" your love score {love_score}")
    
elif (love_score >= 40) and (love_score <= 50) :
    print(f" your love score {love_score}")
else:
    print(f" your love score {love_score}")