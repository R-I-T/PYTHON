# Program to Create a list of colors from comma-separated 
# color names entered by the user. Display first and last colors.

# Function to find first and last colors in the list
def first_and_last_color(color_list):
    print("First color in the list is:",color_list[0]) # First color in the list
    print("Last color in the list is:",color_list[-1]) # Last color in the list

print("Enter a list of colors separated by commas:")
color_list = input().split(",") # Split the input string into a list separated by commas
first_and_last_color(color_list) # Function call