# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)
# Input: 5 Output: yes

# Решение:

def prime (n, div = 2):
     if n == div:
          return True
     elif n % div == 0:
          return False
     elif div*div > n:
          return True
     return prime (n, div+1)
    
num = 12
print(prime(num))