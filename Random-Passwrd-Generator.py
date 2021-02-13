# RANDOM PASSWORD GENERATOR 
import random

print('RANDOM PASSWORD GENERATOR:')
all_mix_chracters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVXYZ1234567890!@#$%^&*(),.?/"
loop = True

while loop:
    password_len = int(input('How many charcters password do you want? '))
    password_count = int(input('How many password do you want? '))
    
    for x in range(0, password_count):
        password = ' '
        for x in range(0,password_len):
            password_output = random.choice(all_mix_chracters)
            password = password + password_output
        print("Here is your password : ", password)
