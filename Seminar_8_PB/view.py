def show_menu():
    print('0. Показать все контакты')
    print('1. Открыть файл с контактами')
    print('2. Записать файл с контактами')
    print('3. Добавить контакт')
    print('4. Изменить контакт')
    print('5. Удалить контакт')
    print('6. Поиск по контактам')

    choise = int(input('Введите пункт меню: '))
    return choise

def show_phone_book(phone_book):
    if len(phone_book) < 1:
        print('Телефонная книга пуста')
    else:
        for id, item in enumerate(phone_book):
            print(id, *item)

def input_path():
    path = input('Введите имя файла: ')
    return path

def input_contact():
    name_contact = input('Введите имя контакта: ')
    phone_contact = input('Введите номер контакта: ')
    comment_contact = input('Введите комментарий: ')
    return(name_contact, phone_contact, comment_contact)

def input_change():
    id = int(input('Введите номер контакта: '))
    print('Что изменить?')
    choise = input('0 - ФИО, 1 - Телефон, 2 - Комментарий, 3 - Отмена')
    value = input('Введите изменения: ')
    return(id, choise, value)
