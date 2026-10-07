from helpers.io import logger
from helpers.crypt import cript_caesar

logger("Запускаем logger...")

enc_phrase = cript_caesar("Шифрую все символы (буквы, цифры, знаки, пробелы)", 2)
print(enc_phrase)