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
    if choice == 3:
        if os.path.getsize('users.json') == 0:
         print("Ваша телефонная книжка пустая")   
        else:    
            user_info = input("Введите элемент для поиска: ")
            with open('users.json', 'r') as file:
                    data = json.load(file)        
            found = False
            for line in data:
                    if isinstance(line, dict):
                        user_name = str(line.get('user name', '')).lower()
                        user_phone = str(line.get('user phone', '')).lower()
                        user_email = str(line.get('user email', '')).lower()
                    if user_info in user_name or user_info in user_phone or user_info in user_email:
                            print('name:'+" " +user_name+'\n','phone:'+" "+user_phone+'\n','email:'+ " "+user_email)
                            found = True
                            break
            if not found:
                print(f"Контакт с '{user_info}' не найден")  
    if choice == 4:
        try:
            with open('users.json', 'r', encoding='utf-8') as file:
                contacts = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            contacts = []

        search_query = input("Введите имя контакта для удаления: ").lower()
        if not contacts:
            print("Список контактов пуст.")
        else:
            found_contact_indexes = []
            for i, contact in enumerate(contacts):
                if search_query in str(contact.get('user name', '')).lower():
                    found_contact_indexes.append(i)

            if found_contact_indexes:
                for i in reversed(found_contact_indexes):
                    deleted_contact = contacts.pop(i)
                    print(f"Контакт '{deleted_contact['user name']}' удален.")
                with open('users.json', 'w', encoding='utf-8') as file:
                    json.dump(contacts, file, ensure_ascii=False, indent=2)
            else:
                print("Контакты не найдены.")                      