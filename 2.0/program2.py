# program that accepts a string from the user and redisplays 
# the string after removing vowels from it

# Getting string from user
str = input("Enter a string: ")

strvowels = str

# Function to remove vowels from string
def remove_vowels(str):
    # Removing vowels from string
    str = str.replace("a", "")
    str = str.replace("e", "")
    str = str.replace("i", "")
    str = str.replace("o", "")
    str = str.replace("u", "")
    str = str.replace("A", "")
    str = str.replace("E", "")
    str = str.replace("I", "")
    str = str.replace("O", "")
    str = str.replace("U", "")
    return str

# Calling function to remove all vowels from string
temp = remove_vowels(str)

# Printing string after removing vowels
print("String after removing vowels from",str,"is:",temp)
