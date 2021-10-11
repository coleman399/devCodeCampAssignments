import re
from fractions import Fraction
email_regular_expression = re.compile(r"[^@]+@[^@]+\.[^@]+")
# 1
print("Question 1") 
users_list = []
target = int(input("target number: "))
users_list_range = int(input("enter number of elements: "))

for element in range(users_list_range):
    element = int(input("enter each element: "))
    users_list.append(element)
# “target - number1 = number2”
def twoSum(users_list, target):
    answer = []

    for element in range(len(users_list)):
        secondNumber = target - users_list[element]
        if secondNumber in users_list:
            secondIndex = users_list.index(secondNumber)
            if users_list[element] + users_list[secondIndex] == target:
                if(element != secondIndex):
                    answer.append(users_list[element])
                    answer.append(users_list[secondIndex])
                    return answer
answer =  twoSum(users_list, target)
print(answer)

# 2
print("Question 2")
users_list = []
answer = False
users_list_range = int(input("enter number of elements: "))
for element in range(users_list_range):
    element = int(input("enter each element: "))
    users_list.append(element)

users_list.sort()
print(users_list)

def check_for_sequence_of_incrementing_integers(list):
    answer = False
    
    for element in range(0, len(list) - 1):
        if list[element] == list[element+1] - 1:
            answer = True
        else:
            answer = False
            return answer
    return answer

answer = check_for_sequence_of_incrementing_integers(users_list)
print(answer) 

# 3
print("Question 3")
users_list = []
users_list_range = int(input("enter number of elements: "))
for element in range(users_list_range):
    element = int(input("enter each element: "))
    users_list.append(element)

def count_pos_and_neg_ints(list):
    pos_count = 0
    neg_count = 0 
    for number in list:
        if number >= 0:
            pos_count += 1
        else:
            neg_count += 1
    list.insert(0, neg_count)
    list.insert(1, pos_count)
    return list

answer = count_pos_and_neg_ints(users_list)
print(answer)

# 4 
print("Question 4")
users_input = input("enter elements separated by a space: ")


def find_high_and_low_number_in_string(string):
    answer = []
    highest_number = 0
    lowest_number = 0
    
    number_list = list(map(int, string.split()))
    number_list.sort()

    highest_number = number_list[-1]
    lowest_number = number_list[0]
    answer = [highest_number, lowest_number]
    return answer

answer_list = find_high_and_low_number_in_string(users_input)
print(f"The highest number in the list is {answer_list[0]}. The lowest number in the list is {answer_list[1]}.")

# 5
print("Question 5")
users_input = input("please provide the email address you would like to verify: ")

def check_if_valid_email(string):
    answer = email_regular_expression.match(string) != None
    if answer is True:
        return answer
    else:
        return answer

answer = check_if_valid_email(users_input)
print(answer)

# 6
print("Question 6")
users_input = input("Replace each letter with its appropriate position in the alphabet: ")

def alphabet_position(string):
    dict = {'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '10', 'k': '11', 'l': '12', 'm': '13',
            'n': '14', 'o': '15', 'p': '16', 'q': '17', 'r': '18', 's': '19', 't': '20', 'u': '21', 'v': '22', 'w': '23', 'x': '24', 'y': '25', 'z': '26'}
    new_string = string.lower()
    new_string = new_string.replace(" ", "")
    string_list = list(new_string)
    for element in string_list:
        if element in dict:
            new_string = new_string.replace(element, dict[element] + " ")
    print(new_string)

alphabet_position(users_input)

# 7
print("Question 7")
users_input = int(input("please enter a 4 digit passcode to get the minimum rotations to unlock briefcase: "))
unlock_code = int(input("please enter a 4 digit unlock code: ")) 
# we are concerned with minimum number of rotation required so we should choose min (abs(a-b), 10-abs(a-b)) as a-b denotes the number of forward rotation and 
# 10-abs(a-b) denotes the number of backward rotation for a ring to rotate from a to b. Further we have to find minimum number for each ring that is for each digit. 
# So starting from right most digit we can easily the find minimum number of rotation required for each ring and end up at left most digit.

# function for min rotation
def minRotation(input, unlock_code):

    rotation = 0

    # iterate till input and unlock
    # code become 0
    while (input > 0 or unlock_code > 0):

        # input and unlock last digit
        # as reminder
        input_digit = input % 10
        code_digit = unlock_code % 10

        # find min rotation
        rotation += min(abs(input_digit - code_digit), 10 - abs(input_digit - code_digit))

        # update code and input
        input = int(input / 10)
        unlock_code = int(unlock_code / 10)

    return rotation

answer = minRotation(users_input, unlock_code)
print(f"Minimum Rotation = {answer}")

# 8
print("Question 8")
users_input = int(input("please provide a number: "))
revs_number = 0

def reverse_number(number):
    global revs_number
    while number > 0:
        remainder = number % 10
        revs_number = (revs_number * 10) + remainder
        reverse_number(number // 10)
        return turn_num_into_reciprocal(revs_number)

def turn_num_into_reciprocal(reversed_number):
    turned_into_reciprocal_string = "1/{}".format(reversed_number)
    turned_into_reciprocal_float = float(Fraction(turned_into_reciprocal_string))
    return turned_into_reciprocal_float

answer = reverse_number(users_input)
print(answer)
