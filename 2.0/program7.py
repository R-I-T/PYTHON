# Program to prompt the user for a list of integers. For all 
# values greater than 100, store ‘over’ instead.

# Function to replace values greater than 100 with 'over'
def over100(list):
    for i in list: # Loop through list
        if i > 100: # Check if value is greater than 100
            list[list.index(i)] = 'over' # if yes, replace with 'over'
    return list # Return list

print("Enter a list of integers separated by spaces: ")
list = [int(i) for i in input().split()] # Get list of integers
print("List of intergers: ", list) # Prints the list
print("List of intergers greater than 100 replaced with over is: ", over100(list)) # Prints the list of intergers greater than 100 replaced with 'over'