from details import shift, normal, cipher
import subprocess
import os

print(len(normal))
print(len(cipher))

def caesar_code(shift):
    print("\nPlease write your message below: ")
    user_input = input("You: ")
    encrypted_message = ""

    for char in user_input:
        if char.isalpha(): # Check if its a letter
            shift_amount = ord('a') if char.islower() else ord('A')
            encrypted_message += chr((ord(char) - shift_amount + shift) % 26 + shift_amount)
        else:
            encrypted_message += char # Non alphabetical chars are not encrypted
            
    print("\nEncrypted Message: \n", encrypted_message)
    
def custom_cipher(normal, cipher):
    print("\nPlease write your message below: ")
    user_input = input("You: ").lower()
    encrypted_index = []
    encrypted_message = ""
    
    for char in user_input:
        if char in normal:
            position = normal.index(char)
            encrypted_index.append(position)
        else:
            print(f"'{char}' is not in the alphabet list.")
    x=0
    for char in encrypted_index:
        encrypted_message += cipher[encrypted_index[x]]
        x+=1
        
    print("\nEncrypted Message: \n", encrypted_message)
        
    
print("\nWhat method of encryption would you like? Caesar Cipher (1), or Custom (2).\n")
answer = int(input("You: "))

while answer != 1 and answer != 2:
    print("Please type a valid input: (1) or (2).")
    answer = int(input("You: "))
    
if answer == 1:
    caesar_code(shift)
elif answer == 2:
    custom_cipher(normal, cipher)
    
print("\nWould you like to go back to the main menu?(Type 1) or Quit (Type 2)?")

answer = int(input("You: "))

while answer != 1 and answer != 2:
    print("Please type a valid input: (1) or (2).")
    answer = int(input("You: "))

if answer == 1:
    subprocess.run(["python", "main.py"])
elif answer == 2:
    os. _exit()