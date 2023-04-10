# Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

# Решение:
userNumber = input("Введите число, сумму цифр которого необходимо посчитать: ")
size = len(userNumber)
sum = 0
for i in range(size):
    sum += int(userNumber[i-1])
print(f"Сумма цифр числа {userNumber} равна {sum}.")