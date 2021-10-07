import random
import datetime
#1
simple_list = ['a' , 'b', 'c', 'd', 'e']   #coding language can apply
user_input = input("please provide input: ")

def compare_user_input_and_list(list, string):
    counter = 0
    for letter in list:
        if string is list[counter]:
            return string
        else:
            counter +=1
    else:
        print("input not in list.")
results = compare_user_input_and_list(simple_list, user_input)
print(results)
#2
min_num = 1
max_num = 100

def random_num_gen_within_range(min, max):
    random_num = random.randint(min,max)
    return random_num
results = random_num_gen_within_range(min_num, max_num)
print(results)
#3
user_input = input("please provide a word you would like to reverse: ")
string_length = len(user_input)

def reverse_word(string, string_length):
    reversed_word = string[string_length::-1]
    return reversed_word
results = reverse_word(user_input, string_length)
print(results)
#4
for count in range(100, 0, -1):
    if(count % 4 == 0 and count % 7 == 0):
        print('Banana')
    elif(count % 4 == 0):
        print('Flamingo')
    elif(count % 7 == 0):
        print('Flamingo-Banana!')
    print(count)
#5
number_list = [1, 2, 3, 7, 8, 9, 45, 134, 43, 2, 3, 1, 6, 7, 5, 4]

def check_for_less(list):
    new_list = []
    counter = 0
    for value in list:
        if list[counter] < 6:
            counter +=1
            continue
        else:
            new_list.append(list[counter])
            counter +=1
            continue
    return new_list 
results = check_for_less(number_list)
print(results)
#6
users_name = input("please provide your name: ")
users_age = input("please provide your age: ")

def findYearWhenAge100(name, age):
    currentTime = str(datetime.datetime.now())
    currentYear = int(currentTime[0: 4])
    age = 100 - int(age)
    currentYear += age
    print(name, "is going to be 100 by", currentYear)
findYearWhenAge100(users_name, users_age)
#7
number_list_1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
number_list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def compare_two_lists(list1, list2):
    compared_list = set(list1) & set(list2)
    return compared_list
results = compare_two_lists(number_list_1, number_list_2)
print(results)
#8
word_one = input("please provide the first word: ")
word_two = input("please provide the second word: ")

def determine_anagram(string1, string2):
    # make both strings lowercase
    string1 = string1.lower()
    string2 = string2.lower()

    # check if length is same
    if(len(string1) == len(string2)):

    # sort the strings
        sorted_str1 = sorted(string1)
        sorted_str2 = sorted(string2)
    # if sorted char arrays are same
        if(sorted_str1 == sorted_str2):
            print(string1 + " and " + string2 + " are anagram.")
        else:
            print(string1 + " and " + string2 + " are not anagram.")
    else:
        print(string1 + " and " + string2 + " are not anagram.")
results = determine_anagram(word_one, word_two)
print(results)