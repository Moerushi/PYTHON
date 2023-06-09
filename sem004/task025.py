# Напишите программу, которая принимает на вход строку,
# и отслеживает, сколько раз каждый символ уже встречался. 
# Количество повторов добавляется к символам с помощью 
# постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию .split()

# Решение 1:
txt = "a a a b c a a d c d d"
initialList = txt.split() # сделали список из строки
someDictionary = dict().fromkeys(initialList, 0)

for i in initialList: # перебираем элементы в списке
    if someDictionary[i] == 0: # если в словаре есть элемент списка i и он равен нулю
        print(i, end = " ") # i это элемент списка
    else:
        print(f"{i}_{someDictionary[i]}", end = " ") # если в словаре есть элемент списка i 
                                                     # и он не равен нулю, то берется значение
                                                     # 
    someDictionary[i] += 1
print(" ")
print(someDictionary)

# # Решение 2:
# stroka = txt.split()
# result = {}
# for i in stroka:
#     if i in result:
#         print(f'{i}_{result[i]}', end=' ')
#     else:
#         print(i, end=' ')
#     result[i] = result.get(i, 0) + 1