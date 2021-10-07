#1
number_list = [1, 2, 2, 4, 5]

def average_of_list(list):
    return sum(list) / len(list)

average = average_of_list(number_list)
print(average)
#2
index = int(input("please provide a number: "))

def index_represented_by_number(list, num):
    if num <= 4 and num > 0:
        print(list[num])
    else:
        print("No value here!")

index_represented_by_number(number_list, index)
#3
def most_frequent_value(list):
    counter = 0
    num = list[0]

    for i in list:
        curr_frequency = list.count(i)
        if(curr_frequency > counter):
            counter = curr_frequency
            num = i

    return num

results = most_frequent_value(number_list)
print(f"The most frequent value of the number list is: {results}")
#4
first_name_list_1 = ['Nevin', 'David', 'Mike']
first_name_list_2 = ['Brett', 'Mike', 'Charles']

# intersection = Return a new set with elements common to the set and all others.
#find common elements of set and list
#Use set() to convert one of the lists to a set. 
#Call set.intersection(*s) on this new set with the other list as *s to find common elements between them. Use list(iterable) to convert the resultant set of common elements to a list.
first_name_list_1_as_set = set(first_name_list_1)
intersection = first_name_list_1_as_set.intersection(first_name_list_2)

intersection_as_list = list(intersection)

print(intersection_as_list)


