number_1 = int(input("Введите первое целое число: "))
number_2 = int(input("Введите второе целое число: "))
number_3 = int(input("Введите третье целое число: "))

if number_1 == number_2 == number_3:
    print(3)
elif number_1 == number_2 or number_2 == number_3 or number_1 == number_3:
    print(2)
else:
    print(0)
