import controller

phone_book = []
path = 'Seminar_8_PB/data/'

def get_phone_book():
    global phone_book
    return phone_book

def set_path(file):
    global path
    # if file not in path:
    path += file

def open_file():
    global path 
    global phone_book
    with open (path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for item in data:
        contact = item.replace('\n', '').split(';')
        phone_book.append(contact)

# set_path("phone_book.txt")
# get_phone_book()
# open_file()
print(phone_book)

def new_contact(contact):
    global phone_book
    phone_book.append(list(contact))

def change_contact(id, choice, value):
    global phone_book
    phone_book [int(id)][int(choice)] = value

def delete_contact(id):
    global phone_book
    phone_book.pop(id)

def search_contact(choiсe, value):
    global phone_book
    search_result = []
    for id, item in enumerate(phone_book):
        if value in item[int(choiсe)]:
            search_result.append(id)
            search_result.append(item)
    return search_result

def save_file():
    global path
    with open(path, 'w', encoding='UTF-8') as data:
        phone_book_save = phone_book_data_create()
        print(phone_book_save)
        data.write(phone_book_save)

def phone_book_data_create():
    global phone_book
    phone_book_save = phone_book
    for index, item in enumerate(phone_book_save):
        phone_book_save[index] = ';'.join(item)
    phone_book_save = '\n'.join(phone_book_save)
    return phone_book_save