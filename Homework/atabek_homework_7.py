from random import randint
from datetime import datetime

secret = randint(1, 100)

number = None
c = 0
start = datetime.now()
while True:
    c += 1
    try:
        number = int(input("Угадайте число(От 0 до 100) "))
        if number > 100:
            print("Вводите число меньше 100!!!")
        elif secret < number:
            print("<")
        elif number < 0:
            print("Введите число больше 0!!!")
        elif secret > number:
            print(">")
        else:
            print(f"Вы угадали🎉 - {secret}")
            break
        if number <= secret + 5 and number >= -5:
            if number < secret:
                print("Очень близко")
            else:
                 print("очень близко")
        elif number <= secret + 10 and number >= secret - 10:
            if number < secret:
                print("близко")
            else:
                print("близко")
    except ValueError:
        print("Введите только числа! ")
end = datetime.now()

print(f"вы были в игре {end - start}" )
print(f"{c} - Попыток")