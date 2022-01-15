# Program that finds whether a given character is present 
# in a string or not. In case it ispresent it prints the 
# index at which it is present. Do not use built in functions 
# to search the character.

# Getting character and string from the user
char = input("Enter a character: ")
string = input("Enter a string: ")

# Function to check character is present in a string or not
def find_character(char):
    for i in range(len(string)): # Iterating through the string
        if string[i] == char: # Checking if the character is present in the string
            print("Character found at index: ",i) # Printing the index at which the character is present
            break
    else: # If the character is not present in the string
        print("Character not found") # Printing character not found

# Calling the function to find character in the string
find_character(char) 