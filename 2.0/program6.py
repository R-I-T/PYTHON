# Program to perform List comprehensions:
# (a) Generate positive list of numbers from a given list of integers
# (b) Square of N numbers
# (c) Form a list of vowels selected from a given word
# (d) Form a list ordinal value of each element of a word (Hint: use ord() to get ordinal values)

# Functions to test the above functions
# Function to generate positive list of numbers from a given list of integers
def positive_list(list):
    return [i for i in list if i>0] # returns numbers which are positive. i.e, number>0

# Function to square of N numbers
def square_list(list):
    return [i**2 for i in list] # returns the square of each element of the list.

# Fucntion to generate vowels list from a given word
def vowel_list(word):
    return [i for i in word if i in "aeiouAEIOU"] # checks if the given word is a vowel or not and if yes,returns it.    

# Function to generate ordinal value of each element of a word
def ordinal_list(word):
    return [ord(i) for i in word] # returns the ordinal value of each element of the word.

print("Enter a list of numbers to generate positive list seperated by spaces: ")
list = [int(i) for i in input().split()] # accepts the list of numbers from the user and splits them into a list.
print("Positive list: ", positive_list(list)) # Function call to generate positive list and prints the result.

print("Enter a list of numbers to generate square list seperated by spaces: ")
list = [int(i) for i in input().split()] # accepts the list of numbers from the user and splits them into a list.
print("Square list: ", square_list(list)) # Function call to generate square list and prints the result.

print("Enter a word to generate vowel list: ")
word = input() # accepts the word from the user
print("Vowel list: ", vowel_list(word)) # Function call to generate vowel list and prints the result.

print("Enter a word to generate ordinal list: ")
word = input() # accepts the word from the user
print("Ordinal list: ", ordinal_list(word)) # Function call to generate ordinal list and prints the result.
