# todo: База данных пользователя.
# Задан массив объектов пользователя

# users = [{'login': 'Piter', 'age': 23, 'group': "admin"},
#          {'login': 'Ivan',  'age': 10, 'group': "guest"},
#          {'login': 'Dasha', 'age': 30, 'group': "master"},
#          {'login': 'Fedor', 'age': 13, 'group': "guest"}]

# Написать фильтр который будет выводить отсортированные объекты по возрасту(больше введеного)
# ,первой букве логина, и заданной группе.

#Сперва вводится тип сортировки:
# 1. По возрасту
# 2. По первой букве
# 3. По группе

# тип сортировки: 1

#Затем сообщение для ввода
# Ввидите критерии поиска: 16

# Результат:
#Пользователь: 'Piter' возраст 23 года , группа  "admin"
#Пользователь: 'Dasha' возраст 30 лет , группа  "master"

users = [{'login': 'Piter', 'age': 23, 'group': "admin"},
          {'login': 'Ivan',  'age': 10, 'group': "guest"},
          {'login': 'Dasha', 'age': 30, 'group': "master"},
          {'login': 'Fedor', 'age': 13, 'group': "guest"}]

sort_type = int(input('''Введите тип сортировки:
  1. По возрасту
  2. По первой букве
  3. По группе
'''))

def print_users(users_array):
  for user in users_array:
      print(f'Пользователь: {user['login']}, возраст: {user['age']} , группа: {user['group']}')


match sort_type:
  case 1:
    age = int(input("Введите критерий поиска: "))
    filtered_users = list(filter(lambda x: x['age'] > age, users))
    sorted_users = sorted(filtered_users, key=lambda x: x['age'])
    print_users(sorted_users)
  case 2:
    latter = input("Введите критерий поиска: ")
    filtered_users = list(filter(lambda x: x['login'][0] == latter, users))
    print_users(filtered_users)
  case 3:
    group = input("Введите критерий поиска: ")
    filtered_users = list(filter(lambda x: x['group'] == group, users))
    print_users(filtered_users)
  case _:
    print('Такого типа сортировки нет!')
