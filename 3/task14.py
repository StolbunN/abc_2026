#todo: Дан массив размера N. Найти минимальное растояние между одинаковыми значениями в массиве и вывести их индексы.
# Одинаковых значение может быть два и более !
# Пример:
# mass = [1,2,17,54,30,89,2,1,6,2]


# Для числа 1 минимальное растояние в массиве по индексам: 0 и 7
# Для числа 2 минимальное растояние в массиве по индексам: 6 и 9
# Для числа 17 нет минимального растояния т.к элемент в массиве один.

mass = [1,2,17,54,30,89,2,1,6,2]

num = int(input("Введите число: "))

if mass.count(num) == 0:
  print(f'Для числа {num} нет минимального растояния т.к элемент нет в массиве.')
elif mass.count(num) == 1:
  print(f'Для числа {num} нет минимального растояния т.к элемент в массиве один.')
else:
  last_index = -1
  minDistance = float('inf')
  distanse_indexes = [-1, -1]
  for index, item in enumerate(mass):
    if item == num:
      if last_index != -1:
        distance = index - last_index
        if minDistance > distance:
          distanse_indexes = [last_index, index]
      last_index = index
  print(f'Для числа {num} минимальное растояние в массиве по индексам: {distanse_indexes[0]} и {distanse_indexes[1]}')
