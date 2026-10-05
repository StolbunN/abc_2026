#todo: Допишите для игры "Поле чудес" функции сохранения и загрузки игры через сериализацию.
# Данные сериализации записываются и сохраняются в файле.

import  random
import json
import os

_dict = {'False': 'Логическое значение', 'None': 'Пустое значение'}
keys = list(_dict.keys())
ind = random.randint(0, len(keys) - 1)
secret = keys[ind]
description = _dict[secret]
mask = [' * '] * len(secret)


def loading_game():
    """Загрузка игры"""
    global secret, description, mask
    while True:
        if os.path.exists("data.json") and os.path.getsize("data.json") > 0:
            print("-"*50)
            loading = input("Хотите выбрать сохранение? (y/n): ").lower()
            print("-"*50)

            if loading == "y":
                with open("data.json", "r") as f:
                    savings = json.load(f)
                    ind = int(input(f"Выберете сохранение от 1 до {len(savings)}: "))
                    save = savings[ind - 1]
                    secret = save["secret"]
                    description = save["description"]
                    mask = list(map(lambda x: f' {x} ', save["current_mask"]))
                    break
            elif loading == "n":
                break
            else:
                print("Неверный ввод. Пожалуйста, введите 'y' (да) или 'n' (нет).")
        else:
            print("Cохранений не найдено. Начало новой игры...")
            break


def show_describe():
    """ Выводит описание слова  """
    print(description)


def show_secret():
    """ Выводит слово """
    for val in mask:
      print(val, end="")


def get_letter():
    letter = input("\n Введите букву: ")
    return letter


def check_letter( letter):
    for ind, val in enumerate(secret):
        if val.upper() == letter.upper():
            mask[ind] = f" {letter} "


def save_game():
    """Сохранение игры"""
    while True:
        print("-"*50)
        save = input("Хотите сохранить игру? (y/n): ").lower()
        print("-"*50)

        if save == "y":
            saving_list = None
            current_mask = "".join(list(map(lambda x: x.strip(), mask)))
            obj = {"description": _dict[secret], "secret": secret, "current_mask": current_mask}

            if os.path.exists("data.json") and os.path.getsize("data.json") > 0:
                with open("data.json", "r", encoding="utf-8") as f:
                    try:
                        saving_list = json.load(f)
                        if not isinstance(saving_list, list):
                            saving_list = [saving_list]
                    except json.JSONDecodeError:
                        saving_list = []
            else:
                saving_list = []

            saving_list.append(obj)
            with open("data.json", "w", encoding="utf-8") as f:
                json.dump(saving_list, f, indent=4)
            print("Игра сохранена!")
            break
        
        elif save == "n":
            break
        else:
            print("Неверный ввод. Пожалуйста, введите 'y' (да) или 'n' (нет).")


def start():
    loading_game()

    print("-"*50)
    print("Если захотите выйти, наберите - exit")
    print("-"*50)

    show_describe()
    while ( " * " in mask):
        show_secret()
        letter = get_letter()
        if letter == "exit":
            save_game()
            break;
        check_letter(letter)
    if(" * " not in mask):
        show_secret()
        print("\nВы выиграли!!!")


start()