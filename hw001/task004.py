# Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?
# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10

# Решение:
totalCranes = int(input("Введите общее кол-во сделанных журавликов: "))
print(f"Петя сделал {totalCranes//6} жур.")
print(f"Сережа сделал {totalCranes//6} жур.")
print(f"Катя сделала {(totalCranes//6)*4} жур.")