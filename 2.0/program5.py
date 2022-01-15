# Program to Create a string from the given string 
# where the first and last character are exchanged.

# Getting string from the user
str = input("Enter a string: ")

def create_string(str): # Function to create a string with first and last character exchanged
    return str[-1] + str[1:-1] + str[0] # return the string with the first and last character exchanged

# Printing the string
print(str,"=>",create_string(str))