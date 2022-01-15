# Store a list of first names. Count the occurrences of 
# ‘a’ within the list.

# Function to count the occurrences of 'a' in the list
def occurences_of_a(list):
    count = 0 # Initialize the count as 0
    for i in list: # Iterate through the list
        if i == 'a': # check if the element is 'a'
            count += 1 # if yes, increment the count by 1
    return count 

print("Enter a list of first names seperated by spaces: ")
list = input() # input the list of first names without splitting
print("The number of occurences of 'a' is: ", occurences_of_a(list)) # Function call