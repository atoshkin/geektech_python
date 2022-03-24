from datetime import datetime
from random import choice
asked_students = []
students = [
    {2: 'Эдил'},
    {4: 'Амантур'},
    {6: 'Аман'},
    {7: 'Эдил'},
    {10: 'Атабек'},
    {11: 'Исмет'},
    {12: 'Дильяр'},
    {13: 'Сыргабек'},
]

while 1:
    random_student = students.index(choice(students))
    print(students.pop(random_student))
    # asked_students.append(random_student)
    rate = input(f'Поставьте оценку: {students[random_student]} ')

    for i in asked_students:
        for k, v in i.items():
            print(f'{k},{v}')

