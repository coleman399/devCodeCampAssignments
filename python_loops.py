# For Loops
#1
for hello in range(5):
    print("Hello")
#2
for count in range(11):
    print(count)
#3
for count_backwards in range(10, -1, -1):
  print(count_backwards)
#4
loop_count = int(input("How many times would you like to loop function? "))
for count in range(loop_count):
    print("devCodeCamp")
#5
for count in range(11):
    print(count)
#6
for character in "Packers":
    print(character)
#7
for count in range(101):
    if(count % 3 == 0 and count % 5 == 0):
        print('fizzbuzz')
    elif(count % 3 == 0):
        print('fizz')
    elif(count % 5 == 0):
        print('buzz')
    print(count)
# While loops
#1
myvariable = 5
while myvariable > 0:
  print("Hello!")
  myvariable -= 1
#2
password = "password"
password_attempt = input("Please enter your password: ")
while password_attempt != password:
    password_attempt = input("Please enter your password: ")
else:
    print("User Validated")
