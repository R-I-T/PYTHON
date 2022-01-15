# Program to accept a list of words and return the length of the longest word.

# Function to find the ength of the longest word 
def longest_word(words):
    longest = 0 # Initialize the longest word length to 0
    for word in words: 
        if len(word) > longest: # If the length of the current word is greater than the longest word length
            longest = len(word) # Set the longest word length to the length of the current word
            longest_word = word # Set the longest word to the current word
    print("Longest word is",longest_word) # Print the longest word
    print("Length of longest word is",longest) # Print the length of the longest word

print("Enter a list of words separated by spaces: ") 
words = input().split() # Get the list of words from the user
longest_word(words) # Function call