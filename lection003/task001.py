# создание функций
import function_file


def sumNumbers(n):
    summa = 0
    for i in range(1, n+1):
        summa += i
    print(summa)


n = 5
sumNumbers(n)

# модульность проектов Python
# обязательное указание с помощью import необходимого файла

print(function_file.f(1))
print(function_file.f(2.3))
print(function_file.f(28))

print(function_file.newString("*", 10))
print(function_file.newString("-"))

print(function_file.concatenatio("a", "s", "d", "w", "e"))

list = []  # создание последовательности Фибоначчи
for i in range(1, 10):
    list.append(function_file.fib(i))
print(list)

print(function_file.quicksort([10, 5, 2, 3]))  # быстрая сортировка

nums = [38, 27, 43, 3, 9, 82, 10]  # сортировка слиянием
print(nums)
function_file.mergeSort(nums)
print(nums)
