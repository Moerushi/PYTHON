# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N].
# Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X
# 5 - это число элементов
# 12345 - это элементы
# 3 - ввод числа на проверку
# -> 1 - ответ = кол-во повторений в ряде

# Решение:
import random
n = int(input("Введите количество элементов списка: "))
x = int(input("Введите число, количество повторений которого нужно посчитать: "))
count = 0 
someList = []
for i in range(n):
    someList.append(random.randint(1,10))
    if x == someList[i]:
        count += 1
print(f"Число {x} в списке {someList} повторяется {count} раз(а).")

