#1 Write a method that determines if a number is happy or sad
#isHappyNumber() will determine whether a number is happy or not
def isHappyNumber(num):
    rem = sum = 0
    #Calculates the sum of squares of digits
    while(num > 0):
        rem = num % 10
        sum = sum + (rem*rem)
        num = num//10
    return sum
num = int(input("please provide a number you would like to check if it is a happy or sad number: "))
result = num
while(result != 1 and result != 4):
    result = isHappyNumber(result)
#Happy number always ends with 1
if(result == 1):
    print(str(num) + " is a happy number")
#Unhappy number ends in a cycle of repeating numbers which contain 4
elif(result == 4):
    print(str(num) + " is not a happy number")
#2 Write a method that prints out all prime numbers between 1 and 100
print("ALL PRIME NUMBER BETWEEN 1 AND 100 GOOOOOOOOOOOOOOOOOOOOOOOOOO!")
for number in range(1, 101):
    count = 0
    for i in range(2, (number//2 + 1)):
        if(number % i == 0):
            count = count + 1
            break
        if (count == 0 and number != 1):
            print(" %d" % number, end = '  ')
#3 : Write a method that does the Fibonacci sequence starting at a number that a user inputs
# Python program to display the Fibonacci sequence
def recur_fibo(new_number, old_number):
    if new_number <= 0:
        new_number = input("please enter a positive number. ")
    else:
       return new_number + old_number
nterms = int(input("\nhow many terms would you like to see of the Fibonacci sequence? "))
starting_number = int(input("what number would like to start the Fibonacci sequence? "))
count = 1
fib_list = []
fib_list.append(starting_number)
# check if the number of terms is valid
if nterms <= 0:
    print("Plese enter a positive integer: ")
else:
    print("Fibonacci sequence:")
    while i in range(nterms):
        if count <= nterms:
            fib_list.append(recur_fibo(fib_list[count-1], fib_list[count-2]))
            count += 1
        else:
            print(fib_list)
            break