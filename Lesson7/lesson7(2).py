from datetime import datetime
import time


print(datetime.now())
# print('Сейчас пройдет сколько-то секунд')
for i in 'Сейчас пройдет сколько-то секунд':
    time.sleep(0.1)
    print(i, end='')





# print("А тольrо теперь сработает")
# print(datetime.now())
# print(time.time())
