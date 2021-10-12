# 1 
print("Question 1")
users_input = int(input("please provide a year: "))
leap_year_list = []

def check_if_leap_year(year):
    global leap_year_list
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                leap_year_list.append(year)
            else:
                return
        else:
            leap_year_list.append(year)
    else:
        return

last_year = users_input + 20

for year in range(users_input, last_year):
    check_if_leap_year(year)

print(leap_year_list)
# 2 
print("Question 2")
users_input = input("please provide a string to find the longest palindomic substring: ")

def longestPalSubstr(string):
    maxLength = 1

    start = 0
    length = len(string)

    low = 0
    high = 0

    # One by one consider every character as center point of
    # even and length palindromes
    for i in range(1, length):
        # Find the longest even length palindrome with center
        # points as i-1 and i.
        low = i - 1
        high = i
        while low >= 0 and high < length and string[low] == string[high]:
            low -= 1
            high += 1

        # Move back to the last possible valid palindrom substring
        # as that will anyway be the longest from above loop
        low += 1
        high -= 1
        if string[low] == string[high] and high - low + 1 > maxLength:
          start = low
          maxLength = high - low + 1

        # Find the longest odd length palindrome with center
        # point as i
        low = i - 1
        high = i + 1
        while low >= 0 and high < length and string[low] == string[high]:
            low -= 1
            high += 1

        # Move back to the last possible valid palindrom substring
        # as that will anyway be the longest from above loop
        low += 1
        high -= 1
        if string[low] == string[high] and high - low + 1 > maxLength:
          start = low
          maxLength = high - low + 1

    print("Longest palindrome substring is:", string[start:start + maxLength])

    return maxLength

# Driver program to test above functions
print("Length is: " + str(longestPalSubstr(users_input)))

# 3
print("Question 3")
users_input = int(input("please provide the number of minutes to would like to convert to hours and minutes: "))

def convert_to_hours(minutes):
        time = int(minutes)
        hour = time // 60
        minutes = time % 60
        time %= 60
        seconds = time
        if minutes != 0:
            return "%dH %dM %dS" % (hour, minutes, seconds)
        elif minutes == 0 and hour != 0:
            return "%dH %dM %dS" % (hour, minutes, seconds)
        elif minutes == 0 and hour == 0 and minutes != 0:
            return "%dM %dS" % (minutes, seconds)
        else:
            return "%dS" % (seconds)

print(convert_to_hours(users_input))

# 4
print("Question 4")
users_input = input("please provide a number to get the difference between it and 13. If the number us greater than 13 the program will return the remainder doubled: ")