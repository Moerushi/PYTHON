# Задача 18: Требуется найти в массиве A[1..N] 
# самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – 
# количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
# 5 - кол-во элементов
# 12345 - элементы (случайно)
# 6 - ввод числа пользователя
# -> 5 - ближайшее число

import random
n = int(input("Введите количество элементов списка: "))
x = int(input("Введите значение, которому необходимо найти близкое по значению число: "))

someSet = set()
while len(someSet) < n:
    someSet.add(random.randint(1,100))

someList = list(someSet)

dif = x

for i in range(n):
    if someList[i] < x and dif > x - someList[i]:
        dif = x - someList[i]
        heighbor = someList[i]
    elif someList[i] > x and dif > someList[i] - x:
        dif = someList[i] - x
        heighbor = someList[i]
    elif someList[i] == x:
        dif = 0 
        heighbor = x

print(f"Перечень: {someList}")
print(f"Ближайшее к числу {x} число: {heighbor}")
