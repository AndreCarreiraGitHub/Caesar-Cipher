import subprocess

print("\nWould you like to Encrypt Data (Type 1) or Decrypt Data (Type 2)?")

answer = int(input("You: "))

while answer != 1 and answer != 2:
    print("Please type a valid input: (1) or (2).")
    answer = int(input("You: "))

if answer == 1:
    subprocess.run(["python", "encrypter.py"])
elif answer == 2:
    subprocess.run(["python", "decrypter.py"])