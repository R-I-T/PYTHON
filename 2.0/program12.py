# Program to read two lists color-list1 and color-list2. 
# Print out all colors from color-list1 not contained in color-list2.

# Function to check if a color contains in both lists
def color_not_in_list(color_list1, color_list2):
    for color in color_list1: # Loop through color_list1
        if color not in color_list2: # Loop through color_list2
            print(color,end=" ") # Print out color if in color_list1 and not in color_list2 

print("Enter the first list of colors seperated by spaces: ")
color_list1 = input().split()
print("Enter the second list of colors seperated by spaces: ")
color_list2 = input().split()
print("Color not in list 2 are: ",)
color_not_in_list(color_list1, color_list2) # Call function
