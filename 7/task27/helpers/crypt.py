def cript_caesar(string, shift=4):
  result = []

  for letter in string:
    code = ord(letter)
    enc_letter = chr(code + shift)
    result.append(enc_letter)

  return ''.join(result)