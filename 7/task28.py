# #todo: Числа в буквы
# Замените числа, написанные через пробел, на буквы. Не числа не изменять.

# Пример.
# Input	                            Output
# 8 5 12 12 15	                    hello
# 8 5 12 12 15 , 0 23 15 18 12 4 !	hello, world!

def get_from_numbers_to_word(string: str):
  result = []

  num_list = string.split(" ")
  for item in num_list:
    if item.isdigit():
      num = int(item)
      if num == 0:
        result.append(" ")
      else:
        result.append(chr(num + 96))
    else:
      result.append(item)
  
  return ''.join(result)

print(get_from_numbers_to_word("8 5 12 12 15"))
print(get_from_numbers_to_word("8 5 12 12 15 , 0 23 15 18 12 4 !"))
