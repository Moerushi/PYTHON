# Написать функцию, которая принимает список строк и возвращает список строк, 
# содержащих только одно слово, с использованием лямбда-функции:

# strings = ["Hello, world!", "This is a sentence.", "Another sentence"]

# Решение:

def removeSymbol(str):
    symbolToRemove = ',.!'
    for symbol in symbolToRemove:
      str = str.replace(symbol,'')
    return str

initialList = ["Hello, world!", "This is a sentence.", "Another sentence"]
newLine = removeSymbol(' '.join(initialList).lower()).split()
for i in newLine:
   print(i)