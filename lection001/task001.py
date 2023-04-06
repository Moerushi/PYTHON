print(1) # выводит данные

var1 = 123
var2 = 1.23
var3 = 3
print(var1, var2, var3)

# var4 = int(input()) считывает данные
var4 = 4
print(var4)

value = None # позволяет создавать переменную с пустым значением
value = var1 + var2 + var3 + var4
print(value)
print(type(value)) # узнает тип данных переменной

line1 =  "hello," # создание переменной со строковым значением
line2 = 'world' # создание переменной со строковым значением
print(line1, line2)

line3 = '\"world\"' # для написания кавычек нужен \
print(line3)

a = 11
b = 2
s = 2022
print(a, b, s)
print(a, "-", b, "-", s) # интерполяция
print('{} - {} - {}'.format(a,b,s)) # интерполяция
print(f'first - {a}, second - {b}, third - {s}') # интерполяция

newLine = '123456'
newInt = int(newLine) # перевод из любого типа данных в число
print(type(newInt))
convertNewLine = str(newInt) # перевод из любого типа данных в строковое значение
print(type(convertNewLine))
newFloat = float(convertNewLine) * 1.34 # перевод из любого типа данных в значение с плавающей запятой
print(f'Конвертация значения {convertNewLine} в Float и умножение на 1.34 = {newFloat}')
print(type(newFloat))

print(f'Сложение a({a}) и b({b}) = {a + b}')
print(f'Вычитание b({b}) из a({a}) = {a - b}')
print(f'Умножение a({a}) на b({b}) = {a * b}')
print(f'Деление (по умолчанию в вещественных числах) a({a}) и b({b}) = {a / b}')
print(f'Остаток от деления a({a}) на b({b}) = {a % b}')
print(f'Целочисленное деление a({a}) на b({b}) = {a // b}')
print(f'Возведение a({a}) в степень b({b}) = {a ** b}')

someFloat = 3.145687445983
print(round(someFloat,3)) # округление до 3 знаков

if a > b:
    print(f'{a} > {b}')
else:
    print(f'{b} > {a}')

if a > b:
    print(f'{a} > {b}')
elif a < s:
    print(f'{s} > {a}')
else:
    print(f'{b} > {a}')

i = 1
while i <= 10:
    print(f"Итерация № {i}")
    i += 1

for z in range(1,11): # создание диаазона через range
    print(z)

r1 = range(5) # диапазон 0 1 2 3 4
r2 = range(2, 5) # диапазон 2 3 4
r3 = range(-5, 0) # диапазон ----
r4 = range(1, 10, 2) # диапазон 1 3 5 7
r5 = range(100, 0, -20) # диапазон 100 80 60 40 20
print(type(r1))

text = 'СъЕШЬ ещё этих МяГкИх французских булок'
print(len(text)) # определение длинны строки
print('ещё' in text)  # проверка на наличие символа в строке
print(text.lower()) # изменение регистра на нижний
print(text.upper()) # изменение регистра на верхний
print(text.replace('ещё','ЕЩЁ')) # замена одного слова другим

print(text[0]) # первый символ строки
print(text[1]) # второй символ строки
print(text[len(text)-1]) # первый символ с конца строки
print(text[-5]) # пятый символ с конца строки
print(text[:]) # вывод всей строки
print(text[:2]) # вывод двух первых символов
print(text[len(text)-2:]) # вывод двух символов с конца строки
print(text[2:9]) # вывод символов со 2 по 9
print(text[6:-18]) # вывод символов с 6 по 18 с конца
print(text[0:len(text):6]) # вывод каждого 6ого символа с 0 до конца строки
print(text[::6]) # вывод каждого 6ого символа с 0 до конца строки
