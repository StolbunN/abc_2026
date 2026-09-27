#todo: Выведите все строки данного файла в обратном порядке, допишите их в этот же файл.
# Для этого считайте список всех строк при помощи метода readlines().

#Содержимое файла inverted_sort.txt
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.

# # Результат
# Complex is better than complicated.
# Simple is better than complex.
# Explicit is better than implicit.
# Beautiful is better than ugly.

with open('inverted_sort.txt', 'a+') as file:
  file.seek(0)
  lines = file.readlines()

  if not lines[-1].endswith('\n'):
    file.write('\n\n')
  elif lines[-1].endswith('\n'):
    file.write('\n')

  lines.reverse()

  for line in lines:
    if not line.endswith('\n'):
      file.write(f'{line}\n')
      print(line)
    else:
      file.write(line)
      print(line[:-1])