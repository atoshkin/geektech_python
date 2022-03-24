
########lambda argument(s): expression#########

# nominal = ["Т.Молдо", "К. Датка", "Т.Сатылганов", "А.Осмонов", "С.Каралаев"]
# number = [20, 50, 100, 200, 500]
#
# # filtered = list(filter(lambda x: x > 100, number))
# # print(filtered)
#
# filtered = list(filter(lambda x: len(x) > 9, nominal))
# print(filtered)
#
#
# square = list(map(lambda x: x * x, number))
# print(square)
#


# info = dict(zip(number, nominal))
# # info = list(zip(number, nominal))
# print(info)
#
# c = 0
# while c != len(nominal):
#     info.update({number[c], nominal[c]})
#     c += 1
#
# print(info)
# c = 0
# while c != len(nominal):
#     info = dict(number=number[c], nominal=nominal[c])
#     c += 1
#
# print(info)

# def square(number):
#     return number ** 2
#
# print(square(6))

# a = lambda x, y: x+y
#
# print(a(5,4))
# def square(number):
#     return number ** 2
#
# print(square(5))
#
# square1 = lambda number:number ** 2
#
# print(square1(5))
# list1 = ['python', 'exceptios', 'lambda']
# list2 = ['functions', 'arguments', 'keyword arguments']
#
#
# def edit(words, a=lambda word: word.capitalize()):
#     for word in words:
#         print(a(word))
#
#
# edit(list1,)
# edit(list2,)
#
#
# # def edit(words,func):
# #     for word in words:
# #         print(func(word))
# # def up_letter(word:str):
# #     return word.capitalize()
