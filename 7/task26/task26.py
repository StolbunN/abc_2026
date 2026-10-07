#todo Задача 1. Чтение матрицы, load_matrix(filename)
# Дан файл, содержащий таблицу целых чисел вида
# (в каждой строке через пробел записаны числа)

# 11 12 13 14 15 16
# 21 22 23 24 25 26
# 31 32 33 34 35 36


# Требуется написать функцию load_matrix(filename) которая загружает эту таблицу из файла.
# Если в каждой строке находится одинаковое количество чисел, функция возвращает список списков целых чисел.
# В противном случае возвращает False.

# Задачу следует решить с использованием списковых включений, циклы использовать НЕЛЬЗЯ!

def load_matrix(filename):
  with open(filename, "r") as f:
    lines = f.readlines()
    count_row = len(lines)
    without_n = [line[:-1].strip() if '\n' in line else line.strip() for line in lines]
    length_row = len(without_n[0].split(" "))
    count_num_in_each_row = [len(line.split(' ')) for line in without_n]
    if count_num_in_each_row.count(length_row) == count_row:
      return without_n
    else:
      return False

print(load_matrix("matrix.txt"))