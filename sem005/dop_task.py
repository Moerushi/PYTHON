# Написать факториал числа

# Решение:

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


num = int(input("Введите число: "))
print(f"{num}! = {factorial(num)}")