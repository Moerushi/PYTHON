# Дополнить телефонный справочник возможностью изменения и 
# удаления данных. Пользователь также может ввести имя или 
# фамилию, и Вы должны реализовать функционал для изменения и удаления данных.

# Решение:

def show_menu() -> int:
    print("\nВыберите необходимое действие:\n" # work_with_phonebook
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Сохранить справочник в текстовом формате\n"
          "6. Удалить пользователя\n"
          "7. Изменить данные пользователя\n"
          "8. Закончить работу"
          )
    choice = int(input())
    return choice
    
def work_with_phonebook():
    choice = show_menu()
    phone_book = read_csv('sem008/phonebook.csv') # DONE
    while (choice != 8):
        if choice == 1:
            show_phonebook(phone_book)
        elif choice == 2:
            name = get_user_input()
            show_phonebook(find_by_name(phone_book, name))
        elif choice == 3:
            number = get_user_input()
            show_phonebook(find_by_number(phone_book, number))
        elif choice == 4:
            user_data = get_new_user()
            add_user(phone_book, user_data)
            write_csv('sem008/phonebook.csv', phone_book)
        elif choice == 5:
            file_name = 'sem008/' + get_user_input()
            write_txt(file_name, phone_book)
        elif choice == 6:
            delete_user(phone_book)
            write_csv('sem008/phonebook.csv', phone_book)
        elif choice == 7:
            change_userdata(phone_book)
            write_csv('sem008/phonebook.csv', phone_book)
        choice = show_menu()

def read_csv(filename: str) -> list:
    data = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
    return data

def print_result(someDict: dict):
    print("~"*10)
    for key in someDict:
        print(f"{key}: {someDict[key]}")
    print("~"*10)

def show_phonebook(phone_book: list):
    for elem in phone_book:
        print_result(elem)
        print()

def get_user_input():
    return input("Введите данные: ")

def find_by_name(phone_book: list, name: str):
    results = []
    for elem in phone_book:
        if elem['Фамилия'] == name:
            results.append(elem)
    return results

def find_by_number(phone_book: list, number: str):
    results = []
    for elem in phone_book:
        if elem['Телефон'] == number:
            results.append(elem)
    return results

def get_new_user():
    record = dict()
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    for field in fields:
        record[field] = input(f'Введите {field}')
    return record

def add_user(phone_book:list,record:dict):
    phone_book.append(record)

def write_txt(filename: str, data: list):
    with open(filename, 'w', encoding='utf-8') as fout:
        for i in range(len(data)):
            s = ''
            for v in data[i].values():
                s += v + ','
            fout.write(f'{s[:-1]}\n')

def write_txt(filename: str, data: list):
    with open(filename, 'w', encoding='utf-8') as fout:
        for i in range(len(data)):
            s = ''
            for v in data[i].values():
                s += v + ','
            fout.write(f'{s[:-1]}\n')

def write_csv(filename: str, data: list):
    with open(filename, 'w', encoding='utf-8') as fout:
        for i in range(len(data)):
            s = ''
            for v in data[i].values():
                s += v + ','
            fout.write(f'{s[:-1]}\n')

def delete_user(phone_book):
    user = input('Введите фамилию абонента, которого необходимо удалить: ')
    for elem in phone_book:
        for v in elem.values():
            if v == user:
                phone_book.remove(elem)

def change_userdata(phone_book):
    user = input('Введите имя пользователя, чьи данные необходимо изменить: ')
    changed_atr = input('Введите изменяемый параметр: ')
    new_atr = input('Введите новое значение параметра: ')
    for elem in phone_book:
        for v in elem.values():
            if v == user:
                elem[changed_atr] = new_atr

work_with_phonebook()