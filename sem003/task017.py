# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4] Output: 6
# Примечание: Пользователь может вводить значения списка или список задан изначально.

# Решение (1 способ через множества):
someList = [1, 1, 2, 0, -1, 3, 4, 4, 6]
someSet = set(someList)
print(f"1 способ (через множества): количество уникальных значений: {len(someSet)} = {someSet}.")

# Решение (1 способ через множества):
secondList = [1, 1, 2, 0, -1, 3, 4, 4, 6]
newSecondList = []

for i in secondList: 
    if i not in newSecondList:
        newSecondList.append(i)
        
print(f"2 способ (через алгоритм): количество уникальных значений: {len(newSecondList)} = {newSecondList}.")