# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k),
# не превосходящие числа N.
# 10 -> 1 2 4 8

# Решение:
n = int(input('Введите число, до которого необходимо рассчиать квадрат числа 2: '))
counter = 0
print("Ответ:", end = " ")
while 2**counter <= n:
    print(f"{2** counter}", end = " ")
    counter += 1
print()