# Program to Count the number of characters (character frequency) in a string.

# Function to count the character frequency in a string
def count(str):
    dict = {} # Dictionary to store the character frequency
    for n in str: # Loop to iterate through the string
        keys = dict.keys() # Get the keys of the dictionary
        if n in keys: # If the character is already present in the dictionary
            dict[n] += 1 # Increment the value of the character
        else: 
            dict[n] = 1 # Else, add the character to the dictionary
    return dict # Return the dictionary

print("Enter a string: ")
str = input()
print("Character frequency in string",str,"is",count(str))
