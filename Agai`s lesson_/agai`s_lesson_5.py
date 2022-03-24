# a = 1, 2, 3, 4, 5
#
# for i in a:
#     if i == 4:
#         print(i)
#     else:
#         print('это не 4')
#
#
#
#
# students = [
#     {'name': 'Dilyar', 'h_w': 5, 'deadline': True, 'points': 39, 'last_rate': 10},
#     {'name': 'Aman', 'h_w': 5, 'deadline': True, 'points': 39, 'last_rate': 10},
#     {'name': 'Amantur', 'h_w': 5, 'deadline': False, 'points': 39, 'last_rate': 10},
#     {'name': 'Atabek', 'h_w': 5, 'deadline': False, 'points': 39, 'last_rate': 10}
# ]
#
# # students[0]['name'] = 'Amanbek'
#
#
# def find_student(name):
#     for i in students:
#         if name in i.values():
#             return i
#         else:
#             print('НЕ найден')
#
#
# def edit(name, new_name):
#     if find_student(name):
#         print(students.index(find_student(name)))
#         students[students.index(find_student(name))]['name'] = new_name
#     else:
#         print('No student')
#
# # edit('Atabek', 'Amanbek')
#
#
# def delete(name):
#     if find_student(name):
#         students.remove(find_student(name))
#     else:
#         print('No student')
#
#
# def checker():
#     for i in students:
#         if i['deadline'] == True:
#             i['last_rate'] = 10
#             i['points'] += i['last_rate']
#         else:
#             i['last_rate'] = 5
#             i['points'] += i['last_rate']
#
# for i in students:
#     print(i)


# def car(**kwargs):
#     return kwargs
#
#
# print(car(mark='Mercedes-Benz', model='w212', color='white'))


# def plus(a, b=2, *args):
#     return sum(args) * a + b
#
#
# print(plus(5, 2, 4, 3))



def greeting(name='Rick'):
    print(f"Hello, {name}")
#
# greeting('Azamat')
# greeting('Aman')
# greeting()