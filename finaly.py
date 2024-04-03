import json
import os

menu = True
contacts = []
while menu:
    print('Меню\n'
        'Выберите действие: \n'
        'Добавить контакт - нажмите 1:\n'
        'Просмотр контактов - нажмите 2:\n'
        'Поиск контакта - нажмите 3:\n'
        'Удалить контакт - нажмите 4:\n'
        'Изменить контакт - нажмите 5: \n'
        'Выход из меню - нажмите 6 '
        )
    choice = int(input('Введите число: '))
    if choice == 1:
        user_info = {}
        name = input('Введите имя: ')
        user_info["user name"] = name
        print('Хотите добавить номер для данного контакта?\n'
              'Введите "да" или "нет"')
        answ_about_number = input()
        num_adder = True
        user_info["user phone"] = []
        if answ_about_number == "да":
            while num_adder:
                phone_num = input('Введите номер телефона: ')
                user_info["user phone"].append(phone_num)
                print('Хотите добавить еще номер к данному контакту?\n'
                      'Введите "да" или "нет" ')
                repeat_add_num = input()
                if repeat_add_num == "да":
                    continue
                elif repeat_add_num == "нет":
                    num_adder = False
        if answ_about_number == "нет":
            user_info["user phone"].append("пусто")
        print('Хотите добавить email для данного контакта?\n'
              'Введите "да" или "нет"')
        answ_about_email = input()
        if answ_about_email == "да":
            email = input('Введите email: ')
            user_info["user email"] = email
        elif answ_about_email == "нет":
            user_info["user email"] = "пусто"
        contacts.append(user_info)
        with open('users.json', 'w', encoding='utf-8') as file:
            json.dump(contacts, file, ensure_ascii=False, indent=2)
    if choice == 2:
        if os.path.getsize('users.json') == 0:
         print("Ваша телефонная книжка пустая")   
        else:   
           with open("users.json", "r") as read:
                data = json.load(read)            
           for user in data:
                print(user)          