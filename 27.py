def square_value():
    for i in range(0,100000):
        if i % 3 == 0:
            three = open("new.file.3.txt","a")
            multiple_of_3 = {
                "multiple_of_3": i
            }
            three.write(str(multiple_of_3))
            yield multiple_of_3
        elif i % 5 == 0:
            five = open("new.file.5.txt","a")
            multiple_of_5 = {
                "multiple_of_5": i
            }
            five.write(str(multiple_of_5))
            yield multiple_of_5
        elif i % 2 == 0:
            two = open("new.file.2.txt","a")
            multiple_of_2 = {
                "multiple_of_2": i
            }
            two.write(str(multiple_of_2))
            yield multiple_of_2



twenty_seven = square_value()
for i in twenty_seven:
    print(i)