def bubbleSort(mas):
    n = len(mas)

    for num in range(n - 1):
        for j in range(0, n - num - 1):
            if mas[j] > mas[j + 1]:
                mas[j], mas[j + 1] = mas[j + 1], mas[j]

list = [5,2,8,1,3,6,9,0,4]
bubbleSort(list)

print(f"Bubble sort: {list}")


def selection_sort(massive):
    for i in range(0, len(massive) - 1):
        smallest = i
        for j in range(i + 1, len(massive)):
            if massive[j] < massive[smallest]:
                smallest = j
        massive[i], massive[smallest] = massive[smallest], massive[i]

list2 = [5,2,8,1,3,6,9,0,4]
selection_sort(list2)

print(f"selection sort: {list2}")
