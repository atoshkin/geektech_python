# dict = {
#     key: value
# }

car = dict(brand='BMW', model='e34', color='black')
car.update(year=1995)
# print(car.get('obem', 'нет такого'))

car2 = car.copy()
car2['color'] = 'silver'


# print(car.get('model'))

for k, v in car.items():
    print(f'{k}: {v}')


print(car.keys())
print(car.values())

















# student = {
#     'name': 'Argen',
#     'age':20,
#     'skills': ['english', 'programming'],
#     'bad habits': 'smoking',
#     # 1: True,
#     # 2.5: False
# }
# print(deleted)
# print(student)
# student['gender'] = 'male'
# student['age'] = 21
# # del student['bad habits']
# deleted = student.pop('bad habits')
# print(student['name'])
# print(student['skills'][1])
