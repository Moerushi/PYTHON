# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15


# Решение:
a1 = int(input("Введите первый элемент прогрессии: "))
d = int(input("Введите разность: "))
n = int(input("Введите количество элементов для вывода: "))
print("Последовательность:", end = " ")
for i in range(n):
    print(a1 + i * d, end = " ")
print()