import secrets
import string
import random

letters = string.ascii_letters

digits = string.digits

special_chars = string.punctuation

selection_list = letters + digits + special_chars

x = input("Enter something\n")

password_len = 10

password = ''
for i in range(password_len):
    password+= ''.join(secrets.choice(selection_list))

print(password)