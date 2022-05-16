import random

def randomm():
    random_number_1 = random.randint(0, 100)
    random_number_2 = random.randrange(0, 100)
    for i in range(100):
        print(random.randint(0, 100))
        if random_number_1 == i:
            yield f"{random_number_1} {i}"
            break

a = randomm()

for i in a:
    print(i)

