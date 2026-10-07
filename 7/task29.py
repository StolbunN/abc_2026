# #todo: Взлом шифра
# Вы знаете, что фраза зашифрована кодом цезаря с неизвестным сдвигом.
# Попробуйте все возможные сдвиги и расшифруйте фразу.


# grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin.

string = "grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin."

codes = []

for i in range(26):
  for enc_letter in string:
    if enc_letter in [" ", "'", "."]:
      codes.append(enc_letter)
      continue
    code = ord(enc_letter) + (i + 1)
    if code > 122:
      letter = chr(96 + ((code - (122 + i)) + i))
    else:
      letter = chr(code)
    codes.append(letter)
  print(f"{''.join(codes)} - {i + 1}")
  codes = []

# although that way may not be obvious at first unless you're dutch. (СТРОЧКА 20)