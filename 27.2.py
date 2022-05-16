import random

def secure_password_generator():
    for i in range(1000):
        nub = random.randint(100,999)
        great_letter = random.choice("abcdefghijklmnopqrstuvwxyz")
        small_letter = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        item = random.choice(f"{great_letter}{small_letter}{nub}")
        item2 = random.choice(f"{great_letter}{small_letter}{nub}")
        item3 = random.choice(f"{great_letter}{small_letter}{nub}")
        passwor = open("passwords.txt","a")
        passwords = {
            "passwords": f"{item}{item2}{item3}{item3}{item2}{item}{item2}{item}"
        }
        passwor.write(str(passwords))
        yield passwords

password = secure_password_generator()

for i in password:
    print(i)
