# Program that encrypts a message by adding a key value to every 
# character (Caesar Cipher) Hint : Say, if key = 3, then add 3 
# to every character. Use chr() and ord() functions

# Getting string to encrypt and key value from user
str = input("Enter the string to be encrypted: ")
key = int(input("Enter the key value: "))

# Function to encrypt the string
def encrypt(str, key):
    encrypted_str = "" # Initializing encrypted string
    for i in range(len(str)): # Looping through the string
        encrypted_str += chr(ord(str[i]) + key) # Adding key value to each character
    return encrypted_str

print("Encrypted string:", encrypt(str,key)) # Printing encrypted string