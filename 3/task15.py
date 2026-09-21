#todo: Дан целочисленный массив размера N из 10 элементов.
#Преобразовать массив, увеличить каждый его элемент на единицу.

import random

num_array = []
for _ in range(10):
  num_array.append(random.randint(1, 100))

print(f'Исходный массив : {num_array}')

for index, item in enumerate(num_array):
  num_array[index] = item + 1

print(f'Преобразованный массив : {num_array}')