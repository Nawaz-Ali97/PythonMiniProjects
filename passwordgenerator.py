import random

print('Welcome to your random password generator!')

chars = "abedefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVQXYZ1234567890!£$%^&*().,"

number = input("How many passwords do you need? ")
number = int(number)

long = input("How many characters is your password? ")
long = int(long)
print ("Here are your passwords!")
for password in range(number):
    passwords = ""
    for char in range(long):
        passwords += random.choice(chars)
    print (passwords)
