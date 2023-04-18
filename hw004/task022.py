# Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

# Решение:
import random

def FillSet (number):
    someSet = set()
    while len(someSet) < number:
        for i in range(number):
            someSet.add(random.randint(1,20))
    return someSet

firstSetLength = int(input("Введите количество элементов первого множества: "))
secondSetLength = int(input("Введите количество элементов второго множества: "))

firstSet = FillSet(firstSetLength)
secondSet = FillSet(secondSetLength)

print(f"Первое множество: {firstSet}")
print(f"Второе множество: {secondSet}")
print(f"Пересекающиеся элементы двух множеств: {firstSet.intersection(secondSet)}")
print(f"Непересекающиеся элементы двух множеств (из первого): {firstSet.difference(secondSet)}")
print(f"Непересекающиеся элементы двух множеств (из второго): {secondSet.difference(firstSet)}")
print(f"Объединение элементы двух множеств: {secondSet.union(firstSet)}")