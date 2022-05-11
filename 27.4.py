import random

def randomm():
    random_number_1 = random.randint(0, 100)
    for i in range(100):
        if i == random_number_1:
            print(random_number_1)
            yield i

a = randomm()

for i in a:
    print(i)

