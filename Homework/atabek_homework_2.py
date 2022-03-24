while True:
    word = input('Введите слово(напишите "Стоп" если хотите выйти): ')
    if word == "Cтоп":
        break
    string = word.lower()
    count = 0
    list1 = "ауоыиэяюёеaeiou"
    for i in string:
        if i in list1:
            count = count+1
    count2 = 0
    list2 = "бвгджзйклмнпрстфхцчшщbcdfghjklmnpqrstvwxyz"
    for i in string:
        if i in list2:
            count2 = count2+1
    count3 = 0
    list3 = "ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁQWERTYUIOPASDFGHJKLZXCVBNM"
    for i in word:
        if i in list3:
            count3 = count3+1
    count4 = 0
    for i in word:
        if i in list1 or list2:
            count4 = count4+1
print(f"Количество: {count4}")
print(f"Прописные: {count3}")
print(f"Гласные: {count2}")
print(f"Согласные: {count}")
print(f"Гласные: {round(count3 / len(word) * 100, 2)}%")
print(f"Согласные: {round(count2 / len(word) * 100, 2)}%")