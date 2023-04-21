# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на максимальные. 
# Напишите программу, которая заменяет оценки Василия, 
# но наоборот: все максимальные – на минимальные.
# Input: 5 (кол-во оценок) -> 1 3 3 3 4 
# Output: 1 3 3 3 1

# Решение:
import random

def Change(n):
    if n == 0:
      return " "
    mark = int(input(f"Введите оценку: "))
    if mark > 3:
        print(f"Оценка изменена на: {random.randint(1,2)}.")
    else:
        print(f"Оценка не изменена. Текущая: {mark}.")
    return Change(n-1)

n = int(input("Введите количество оценок к изменению: "))
Change(n)