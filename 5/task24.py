# todo: Шифр Цезаря
# Описание шифра.
# В криптографии шифр Цезаря, также известный шифр сдвига, код Цезаря или сдвиг Цезаря,
# является одним из самых простых и широко известных методов шифрования.
# Это тип подстановочного шифра, в котором каждая буква в открытом тексте заменяется буквой на некоторое
# фиксированное количество позиций вниз по алфавиту. Например, со сдвигом влево 3, D будет заменен на A,
# E станет Б, и так далее. Метод назван в честь Юлия Цезаря, который использовал его в своей частной переписке.

# Задача.
# Считайте файл message.txt и зашифруйте текст шифром Цезаря, при этом символы первой строки файла должны
# циклически сдвигаться влево на 1, второй строки — на 2, третьей строки — на три и т.д.
# В этой задаче удобно считывать файл построчно, шифруя каждую строку в отдельности.
# В каждой строчке содержатся различные символы. Шифровать нужно только буквы кириллицы.

# enc_message.txt - зашифрованный текст

import unicodedata

lines = None
count_lines = None

with open('message.txt', 'r', encoding='utf-8') as file:
  lines = file.readlines()
  count_lines = len(lines)


with open('enc_message.txt', 'w', encoding='utf-8') as file:
  for index in range(count_lines):
    string = list(lines[index])
    for letter in string:
      try:
        # проаеряем, что буква - кириллица
        alphabet = unicodedata.name(letter)
        if "CYRILLIC" in alphabet:
          code = ord(letter)
          # обработка буквы Ё
          if code == 1025:
            code = 1046
          # обработка буквы ё
          if code == 1105:
            code = 1078
          enc_index = code - (index + 1)
          # если строчная буква выходит из диапазона, то переносим в конец диапазона строчных букв
          if 1072 <= code <= 1103 and enc_index < 1072:
            enc_index = 1103 - (((code - enc_index) - (code - 1072)) - 1)
          # если заглавная буква выходит из диапазона, то переносим в конец диапазона заглавных букв
          if 1040 <= code <= 1071 and enc_index < 1040:
            enc_index = 1071 - (((code - enc_index) - (code - 1040)) - 1)
          encrypted_letter = chr(enc_index)
          file.write(encrypted_letter)
        else:
          file.write(letter)
      except ValueError:
        file.write(letter)

