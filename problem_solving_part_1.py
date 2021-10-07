#1 Write code that takes a string as input and returns the string reversed
user_input = input("please provide a word you would like to reverse: ")
string_length = len(user_input)

def reverse_word(string, string_length):
    reversed_word = string[string_length::-1]
    return reversed_word
results = reverse_word(user_input, string_length)
print(results)
#2 Write code that takes a string as input and capitalize the first letter of each word
user_input = input("please provide a title you would like to capitalize the first letter of each word: ")
# Capitalize the first letter of each word i.e.
# Convert the first letter of each word to Upper case and all other to lower case
results = user_input.title()
print(results)
#3 Compress a string of characters
user_input  = input("please provide a string you would like to compress: ")

def compress(string):
    """
    This solution compresses without checking. Known as the RunLength Compression algorithm.
    """

    # Begin Run as empty string
    result = ""
    length = len(string)
    
    # Check for length 0
    if length == 0:
        return ""
    # Check for length 1
    if length == 1:
        return string + "1"
    #Intialize Values
    count = 1
    i = 1
    while i < length:
        # Check to see if it is the same letter
        if string[i] == string[i - 1]:
            # Add a count if same as previous
            count += 1
        else:
            # Otherwise store the previous data
            result = result + string[i - 1] + str(count)
            count = 1
            # Add to index count to terminate while loop
        i += 1
    # Put everything back into run
    result = result + string[i - 1] + str(count)
    return result
results = compress(user_input)
print(results)
#4 Write code that takes a user input and checks to see if it is a Palindrome and reports the result
def check_palindrome(string):
    length = len(string)
    first = 0
    last = length - 1
    status = 1
    while(first < last):
        if(string[first] == string[last]):
            first = first+1
            last = last-1
        else:
            status = 0
            break
    return int(status)
string = input("enter the string you would like to check if a palindrome: ")
status = check_palindrome(string)
while status in range(0, 2):
    if (status == 1):
        print("It is a palindrome!")
        break
    else:
        string = input("Sorry! Try again: ")
        status = check_palindrome(string)