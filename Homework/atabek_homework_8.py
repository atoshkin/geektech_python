from random import randint
from datetime import datetime

attempts = int(input("Введите желаемое количество попыток: "))
userName = input("Введите ваше имя: ")

count = 0
start = datetime.now()
with open("result.txt", "w", encoding='UTF-8') as file:
    while attempts != count:
        count += 1

        firstNum = randint(1,9)
        secondNum = randint(1,9)
        rightAnswer = firstNum * secondNum

        userVariant = int(input(f"{firstNum} * {secondNum} = ?: "))

        if rightAnswer == userVariant:
            print(rightAnswer)
            file.write(f"{firstNum} * {secondNum} = {userVariant} ({rightAnswer}) 'правильно'\n")
        elif rightAnswer != userVariant:
            print(rightAnswer)
            file.write(f"{firstNum} * {secondNum} = {userVariant} ({rightAnswer}) 'неправильно'\n")
    end = datetime.now()


    file.write(f"Было-(а,и) {attempts}, попыток-(ки,ка) \nПотрачено время {end - start}, имя: {userName}")