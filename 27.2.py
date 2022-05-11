import random


def secure_password_generator():
    for i in range(1000):
        passwor = open("passwords.txt","a")
        passwords = {
            "passwords": random.randint(0,100000000)
        }
        passwor.write(str(passwords))
        yield passwords

password = secure_password_generator()

for i in password:
    print(i)
