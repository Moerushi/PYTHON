# Вводится список целых чисел в одну строчку через пробел. 
# Необходимо оставить в нем только двузначные числа. 
# Реализовать программу с использованием функции filter. 
# Результат отобразить на экране в виде последовательности оставшихся чисел в одну строчку через пробел.


#  пример -8 11 0 -23 140 1 => 11 -23

# Решение:
import random

someList = [item for item in [random.randint(-20,20) for _ in range(10)]]
print(*someList)
finalList = [item for item in someList if 10 <= abs(item) < 100]

# someList = [int(item) for item in input("Введите через пробел любые числа: ").split()]
# print(*someList)
# finalList = [item for item in someList if 10 <= abs(item) < 100]

# someList = list(map(int,input("Введите через пробел любые числа: ").split()))
# print(*someList)
# finalList = list(filter(lambda item: 10 <= abs(item) < 100, someList))
print(*finalList)