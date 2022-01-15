# Program to Create a single string separated with space 
# from two strings by swapping the character at position 1. 
# Eg : str1 = “Hello” str2 =”World” , then create a string 
# str3 = “Hollo Werld” [Hint: use slicing and concatenation

# Function to swap the character at position 1
def create_string(str1,str2):
    str3 = str1[0] + str2[1] + str1[2:] + " "+ str2[0] + str1[1] + str2[2:] # swap the character at position 1
    return str3

print("Enter the first string: ")
str1 = input()
print("Enter the second string: ")
str2 = input()
print("The string after swapping is: ",create_string(str1,str2)) # call the function