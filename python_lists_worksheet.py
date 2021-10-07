#1
name_list = ['dillon', 'patrick', "coleman"]

def zero_index_of_list(list):
    results = list[0]
    return results

results = zero_index_of_list(name_list)
print(results) 
#2
color_list = ['blue', 'red', 'white', 'green', 'yellow']

def check_if_color_matches(list):
    user_input = input("Please enter a color: ")
    if user_input in color_list:
        print("You found my chosen color")
    else:
        print("Not my chosen color")

check_if_color_matches(color_list)
#3
number_list = [1, 2, 3, 4, 5]

def even_or_odd(list):
    addition = sum(list)
    if (addition % 2) == 0:
        print("Even")
    else:
        print("Odd")

results = even_or_odd(number_list)
print(results)
#4
number_list_two = [1, 2, 3, 4, 5]
def list_numbers_greater_than(list, int):
    for number in list:
        if int < number:
            print(number)

results = list_numbers_greater_than(number_list_two, 1)

