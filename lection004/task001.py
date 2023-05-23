def f(x):
    return x*x

print(f(5))
print(type(f))

a = f  # хранит в себе ссылку
print(type(a))
print(a(5))

def sum (x,y):
    return x + y
# равносильно
sum = lambda x,y: x + y

def math(op, x, y):
    print(op(x, y))
# равносильно
math = lambda a, b: a + b, 5, 45  # какие элементы взять и что с ними сделать
# если используем лямбду более 2 раз, то лучше обычную def функцию

# ~~~~~~~~~~~~~~~
data0 = [1, 2, 3, 5, 8, 15, 23, 38]
out = []
for i in data0:
    if i % 2 == 0:
        out.append((i,i**2))
# def select (f, col):
#     return [f(x) for x in col]
# равносильно
def select (f, col):
    list = []
    for x in col:
        list.append(f(x))
    return list
# равносильно функции map, те применит функцию для каждого x в перечне
res6 = select(int,data0)
print(f"res6 select = {res6}")

# def where (f,col):
#     return [x for x in col if f(x)]
# равносильно
def where (f,col):
    list = []
    for x in col:
       if f(x):
            list.append(x)
    return list
# равносильно функции filter
res6 = where (lambda x: x % 2 == 0, res6)
print(f"res6 where = {res6}")
res6 = list(select(lambda x: (x,x**2), res6))
print(f"res6 square = {res6}")
# ~~~~~~~~~~~~~~~~~~~~~~

data = [1, 2, 3, 5, 8, 15, 23, 38]

list_1 = [x for x in range(1, 20)]  # создает элемент в диапазоне
print(list_1)
# применяет указанную функцию к каждому элементу и возвращает с новыми объектами
list_1 = list(map(lambda x: x + 10, list_1))
print(list_1)

data2 = '1 2 3 5 8 15 23 38'.split()
res1 = map(int, data2)
res1 = filter(lambda x: x % 2 == 0, res1)
res1 = list(map(lambda x: (x, x ** 2), res1))
print(res1)

data3 = [x for x in range(10)]
# возвращает только те значения, которые есть в фильтре
res2 = list(filter(lambda x: x % 2 == 0, data3))
print(res2)

users = ['user1', 'user2', 'user3']
ids = [4,5,9,14,7]
data4 = list(zip(users,ids))
print(data4)

data5 = list(enumerate(['Казань', 'Рыбки', 'Чикаго'])) # создает кортеж и нумерует файлы
print(data5)

# Файлы в текстовом формате используются для:
# - Хранения данных
# - Передачи данных в клиент-серверных проектах
# - Хранения конфигов
# - Логирования действий

# Режими работы с файлами:
# a - добавление в файл / создание файла при его отсутствии
# r - чтение файла / появление ошибки, если файла не существует
# w - запись / каждый раз перезаписывает в файле / создание файла при его отсутствии
# w+ - открытие файла для записи и чтения из него / создает файл при его отсутствии
# r+ - открытие файла для чтения и записи в него / ошибка, если нет файла

color = ['pink ','green ','blue ']
data = open ('lection004/file1.txt', 'w')
data.writelines(color)
data.close

with open ('lection004/file2.txt', 'w') as data:
    data.write('line 1\n')
    data.write('line 2\n')

path = 'lection004/file3.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()

import os # для работы с операционной системой
os.chdir('/Users/nikitamatveev/Documents/Repo/PYTHON') # смена текущей директории
print(os.getcwd()) # текущая рабочая директория
print(os.path.basename("/Users/nikitamatveev/Documents/Repo/PYTHON/lection004/task001.py")) # базовое имя пути
print(os.path.abspath('task001.py')) # возвращает нормализованный абсолютный путь

import shutil # позволяет копировать, перемещать и удалять файлы и папки
# shutil.copyfile(scr,dst) # копирует содержимое (но не метаданные) файла src в файл dst.
# shutil.copy(scr,dst) # копирует содержимое файла src в файл или папку dst
# shutil.rmtree(path) # Удаляет текущую директорию и все поддиректории; path должен указывать на директорию, а не на символическую ссылку