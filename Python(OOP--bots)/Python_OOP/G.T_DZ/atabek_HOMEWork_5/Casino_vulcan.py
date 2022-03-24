import os
import random
from envparse import env


class Casino:
    def __init__(self):
        self.__cash = int(os.environ.get('MY_MONEY'))

        while int(self.__cash) > 0:
            self.__slot = random.randint(1, 30)
            self.__bet = int(input('Делайте ставку : '))
            if self.__bet > self.__cash:
                print('У вас недостаточно денег')
            else:
                self.__choice = int(input('Выберите слот : '))

                if self.__slot == self.__choice:
                    self.__cash += self.__bet
                    print(f'Поздравляем вы выиграли !!! \n Ваш счет : {self.__cash}')
                    if self.__slot == self.__choice:
                        ans = input('Введите cont для продолжение введите end для выхода: ')
                        if ans == 'cont':
                            continue
                        if ans == 'end':
                            break

                else:
                    self.__cash -= self.__bet
                    print(f' К сожалению вы проиграли \n Ваш счет: {self.__cash}')
                    if self.__slot != self.__choice:
                        ans = input('Введите cont для продолжение введите end для выхода: ')
                        if ans == 'cont':
                            continue
                        if ans == 'end':
                            break

    @property
    def slot(self):
        return self.__slot

    @slot.setter
    def slot(self, value):
        self.__slot = value

env.read_envfile('settings.env')