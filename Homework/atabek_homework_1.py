osh = float(input('Температура воздуха в Оше: '))
talas = float(input('Температура воздуха в Талас: '))
chui = float(input('Температура воздуха в Чуй: '))
jalalAbad = float(input('Температура воздуха в Жалал-Абад: '))
naryn = float(input('Температура воздуха в Нарын: '))
issykKol = float(input('Температура воздуха в Ыссык-Кол: '))
batken = float(input('Температура воздуха в Баткен: '))

total = (osh + talas + chui + jalalAbad + naryn + issykKol + batken) /7
print("Средний показатель температуры воздуха по КР на сегодня", round(total,1),"°C")