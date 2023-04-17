# Дана последовательность из N целых чисел и число K. 
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) 
# на K элементов вправо, K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 3 Output: [4, 5, 1, 2, 3]
# Примечание: Пользователь может вводить значения списка или список задан изначально.

# Решение:
someList = [1, 2, 3, 4, 5]
print(someList)
k = 3
for _ in range(k):
    someList.insert(0,someList.pop())
print(someList)