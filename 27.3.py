def step():
    start = int(input("Напишите первое число: "))
    end = int(input("Напишите второе число: "))
    progression = int(input("Напишите чело которое вы хотите использовать для прогресии (необязатель): "))
    print("Что вы хотите сделать")
    item = int(input("1)Вывести 1 число по 2 2)Вывести 2 число по 1 3)Вівести 1 число по 2 с прогресией которую вывели 4) также как и в 3 только 2 числа по 1 : "))
    if item == 1:
        while start < end:
            start += 1
            yield start
    elif item == 2:
        while end > start:
            end -= 1
            yield end
    elif item == 3:
        while start < end:
            start += progression
            yield start
    elif item == 4:
        while end > start:
            end -= progression
            yield end
    else:
        print("Ошибка")

a = step()

for i in a:
    print(i)



