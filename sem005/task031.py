# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1). Требуется найти N-е число Фибоначчи
# Input: 7 Output: 21
# Задание необходимо решать через рекурсию

# Решение:

def Fibonacci (n):
    if n == 1 or n == 2:
      return 1
    else:
      return Fibonacci (n-1) + Fibonacci (n-2)

for i in range (1,10):
    print (Fibonacci(i), end = " ")
print(" ")

