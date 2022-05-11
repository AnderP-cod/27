def step():
    start = int(input("Напишите первое число: "))
    end = int(input("Напишите второе число: "))
    while start < end:
        start += 1
        yield start

a = step()

for i in a:
    print(i)



