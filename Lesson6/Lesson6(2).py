# list_1 = [5, 2.5, 'python', True, (1, 2, 3), {'name', 'surname'}, {'a', 'b', 'c'}]

male = []
female = []
info = {}


try:
    circle = int(input('Введите количество кргуов: '))


    while circle != 0:
        info.append(dict(name=input('Введите имя'), gender=input('Введите пол м/ж')))
        circle -= 1


    for i in info:
        if i ['gender'] == 'м':
            male.append(i)
        else:
            female.append()

except Exception:
    print('Вводить только целые числа')

print(info)






















# numbers = [0, 1, 2, 3, 4, 5]
# numbers_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
#
# try:
#     print(numbers["sdsad"])
# except TypeError:
#     print("Введите только числа")
#
# try:
#     print(numbers[6])
# except IndexError:
#     print(
#         "Нет такого индекса! \n"
#         f"Вводите от 0 до {len(numbers_1) - 1}"
#     )

