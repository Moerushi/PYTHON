# Дан массив, состоящий из целых чисел. 
# Напишите программу, которая в данном массиве определит количество элементов, 
# у которых два соседних и, при этом, оба соседних элемента меньше данного. 
# Сначала вводится число N — количество элементов в массиве 
# Далее записаны N чисел — элементы массива. Массив состоит из целых чисел.

# Ввод: 
# 5
# 1 2 3 4 5
# Вывод:
# 0

# Решение:

someList = list(map(int,input("Введите через пробел числа: ").split()))
counter = 0

for i in range(1,len(someList)-1):
    if someList[i+1] < someList[i] > someList[i-1]:
        counter += 1

print(f"Ваш результат: {counter}")