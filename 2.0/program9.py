# Program to prompt the user to enter two lists of integers and check
# (a) Whether lists are of the same length.
# (b) Whether the list sums to the same value .
# (c) Whether any value occurs in both Lists.

# Function to check whether lists are of the same length
def equal_or_not(list1,list2):
    if len(list1) == len(list2): # check whether lists are of the same length
        print("Lists are of the same length") 
    else:
        print("Lists are not of the same length")

# Function to check whether lists sum to the same value
def sum_list(list1,list2):
    print("Sum of list 1 is:",sum(list1)) 
    print("Sum of list 2 is:",sum(list2))
    if sum(list1) == sum(list2): # check whether lists sum to the same value
        print("Lists sum to the same value")
    else:
        print("Lists do not sum to the same value")

# unction to check whether any value occurs in both lists
def occurrences(list1,list2):
    for i in list1: # iterate through list1 
        if i in list2: # iterate through list2
            print("Value",i,"occurs in both lists")

print("Enter the first list of integers separated by commas:")
list1 = [int(x) for x in input().split()] # Get list1 from user
print("Enter the second list of integers separated by commas:")
list2 = [int(x) for x in input().split()] # Get list2 from user
equal_or_not(list1,list2) # Call function to check whether lists are of the same length
sum_list(list1,list2) # Call function to check whether lists sum to the same value
occurrences(list1,list2) # Call function to check whether any value occurs in both lists
