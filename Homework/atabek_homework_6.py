ten = [1,2,3,4,5,6,7,8,9,10]

evens = list(filter(lambda x: x % 2== 0,ten))
print(evens)

events = list(map(lambda x: x ** 2,evens))
print(events)

def ten1(lst=ten):
    while 1:
        try:
            num = input("введите индекс: ")
            if num == 'stop':
                break
            else:
                print(lst[int(num)])
        except Exception:
            print(f"индекс: от 0 до {len(lst)-1}")
ten1()

