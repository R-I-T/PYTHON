# From a list of integers, create a list after removing even numbers.

# Function to remove even numbers from the list
def remove_even(list):
    for i in list: 
        if i % 2 == 0: # check if the number is even
            list.remove(i) # if yes, remove the number
    return list

print("Enter a list of integers separated by commas: ")
list = [int(i) for i in input().split(',')] # Get the list of integers as integers
print("List of integers after removing even numbers: ",remove_even(list))