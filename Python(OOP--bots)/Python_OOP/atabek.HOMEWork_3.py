class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        return f"CPU * Memory = {self.__cpu * self.__memory}"

    def __str__(self):
        return f"CPU: {self.__cpu} Memory: {self.__memory}"

    def __gt__(self, other):
        return self.memory > other.memory


class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call(self, sim_card_number, call_to_number):
        print(f"Идет звонок на номер {simCard} с сим-карты-{simCard}")

    def __str__(self):
        return f"sim cards list: {self.__sim_cards_list}"


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, *sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def use_gps(self, location):
        print(f"Проложен маршрут до точки: {location}")

    def __str__(self):
        return f"CPU: {self.cpu} \n Memory:{self.memory} \n Sim card: {self.sim_cards_list}"

simCard = ["1 - Tele 2", "Yota"]
lt = Computer(64, 4)
lt.make_computations()
ph = Phone(1)
smartP = SmartPhone(345, 4, simCard[0])
smartP2 = SmartPhone(678, 8, simCard[1])
smartP.call("+8 (843) 2000423", simCard[0])
smartP.use_gps("Казань")


print(lt)
print(lt.make_computations())
print(ph)
print(smartP)
print(smartP2)
print(lt > smartP)