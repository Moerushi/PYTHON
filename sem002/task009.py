# По данному целому неотрицательному n вычислите значение n!. 
# N! = 1 * 2 * 3 * ... * N (произведение всех чисел от 1 до N) 0! = 1 
# Решить задачу используя цикл while
# Input: 5
# Output: 120

# Решение:
n = int(input("Введите число, факториал которого необходимо вычислить: "))
m = n
f = 1
if n == 0 or n == 1:
   print(f"{n}! = 1")
else:   
   while n > 1 :
      f *= n
      n -= 1
   print(f"{m}! = {f}")
