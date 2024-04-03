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
    if choice == 5:
        try:
            with open('users.json', 'r', encoding='utf-8') as file:
                contacts = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            contacts = []
        search_query = input("Введите имя контакта для изменения: ").lower()
        if not contacts:
            print("Список контактов пуст.")
        else:
            found_contacts = []
            indexes_to_modify = []

        for i, contact in enumerate(contacts):
            if search_query in str(contact.get('user name', '')).lower():
                found_contacts.append(contact)
                indexes_to_modify.append(i)
            if found_contacts:
             for i, contact in enumerate(found_contacts, 1):
                print(f"{i}. {contact}")
            index = int(input("Введите номер контакта для изменения: ")) - 1
            if 0 <= index < len(found_contacts):
                modified_contact = found_contacts[index]
                print(f"Выбранный контакт: {modified_contact}")
                print("Выберите, что хотите изменить:\n"
                       "1. Имя пользователя\n"
                       "2. Телефонный номер\n"
                       "3. Электронная почта")
                choice2 = input("Введите номер: ")
                
                if choice2 == "1":
                    new_name = input("Введите новое имя: ")
                    modified_contact["user name"] = new_name
                elif choice2 == "2":
                     modified_contact["user phone"] = []
                     print("Введите новый телефонный номер: ")
                     new_phone1 = input()   
                     modified_contact["user phone"].append(new_phone1)
                     while True:
                            print('Хотите добавить еще телефонный номер к данному контакту?\n'
                                  'Введите "да" или "нет" ')
                            answer = input()
                            if answer.lower() == 'нет':
                                break
                            elif answer.lower() == 'да':
                              new_phone = input('Введите номер: ')
                            modified_contact["user phone"].append(new_phone)
                            with open('users.json', 'w', encoding='utf-8') as file:
                                json.dump(contacts, file, ensure_ascii=False, indent=2)
                elif choice2 == "3":
                        new_email = input("Введите новую электронную почту: ")
                        modified_contact["user email"] = new_email
                else:
                    print("Неверный выбор.")
                contacts[indexes_to_modify[index]] = modified_contact
                with open('users.json', 'w', encoding='utf-8') as file:
                    json.dump(contacts, file, ensure_ascii=False, indent=2)
                print(f"Контакт изменен: {modified_contact}")
            else:
                print("Неверный номер контакта.")
        else:
            print("Контакты не найдены.")
    if choice == 6:
        print("Выход из меню")
        menu = False        