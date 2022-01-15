# Program to Add ‘ing’ at the end of a given string. 
# If it already ends with ‘ing’, then add ‘ly’

# Function to add 'ing'/'ly' at the end of a given string
def add_ing(str):
    if str[-3:] == 'ing': # if the last three characters are 'ing'
        return str + 'ly' # add 'ly' to the end of the string
    else:
        return str + 'ing' # add 'ing' to the end of the string

print("Enter a string: ")
str = input()
print("The string is ",str)
print("The string after adding 'ing'/'ly' is: ", add_ing(str)) # call the function
