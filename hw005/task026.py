# Задача 26: Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

# A = 3; B = 5 -> 243 (3^5)
# A = 2; B = 3 -> 8

# Решение:
a = int(input(f"Введите число для возведения в степень: "))
b = int(input(f"Введите степень: "))
def exponentiation(a, b):
    if b == 1:
      return a
    else:
      return exponentiation(a, b-1) * a

print(f"{a} ^ {b} = {exponentiation(a, b)}")
