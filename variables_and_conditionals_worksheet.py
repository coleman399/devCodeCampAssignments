import random

age = int(input("please provide your age: ")) #1
print(f"I am {age} years old.") 

first_name = input("please enter your first name: ") #2

last_name = input("please enter your last name: ") #3

full_name = first_name + " " + last_name #4
print(f"My first name is {first_name} and my last name is {last_name}, which means my full name is {full_name}")

temperature_input = float(input("Please enter a Fahrenheit temperature that you would like to convert to Celsisus: ")) #5
celsius = (temperature_input - 32) * 5.0/9.0
print(f"{temperature_input} degrees Fahrenheit is {celsius} degrees Celsius")

#Conditionals
legal_driving_age = 18 #1
user_age = int(input("please enter your age of potential driver: "))

if user_age >= legal_driving_age:
    print("You are legally able to drive.")
else:
    print("You are not old enough to drive yet.")


print("Creating a random number.")
random_number = random.randint(1, 10) #2

if random_number <= 2 and random_number >= 0:
    print("0 or 1 or 2")
elif random_number <= 5 and random_number >= 3:
    print("3 or 4 or 5")
elif random_number <= 8 and random_number >= 6:
    print("6 or 7 or 8")
else:
    print("9 or 10")

nfl_team_name = input("please enter an nfl team: ") #3
if nfl_team_name == "Bears":
    print("quarterback much?")
elif nfl_team_name == "Vikings":
    print("loud noises!")
elif nfl_team_name == "Lions":
    print("LOL! They bad!")
elif nfl_team_name == "Packers":
    print("Best team in the world! Actually, the universe")
else:
    print("Pick a different team")
