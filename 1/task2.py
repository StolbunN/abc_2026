# todo: Преобразуйте переменную age и foo в число
# age = "23"
# foo = "23abc"
#
# Преобразуйте переменную age в Boolean
# age = "123abc"
#
# Преобразуйте переменную flag в Boolean
# flag = 1
#
# Преобразуйте значение в Boolean
# str_one = "Privet"
# str_two = ""
#
# Преобразуйте значение 0 и 1 в Boolean
#
# Преобразуйте False в строку

age = "23"
foo = "23abc"           # допустим, что это шестнадцатиричное число
print("Преобразуйте переменную age и foo в число: ", type(int(age)), int(age), type(int(foo, 16)), int(foo, 16))


age = "123abc"
print("Преобразуйте переменную age в Boolean: ", type(bool(age)), bool(age))


flag = 1
print("Преобразуйте переменную flag в Boolean: ", type(bool(flag)), bool(flag))


str_one = "Privet"
str_two = ""
print("Преобразуйте значение в Boolean: ", type(bool(str_one)), bool(str_one), type(bool(str_two)), bool(str_two))


print("Преобразуйте значение 0 и 1 в Boolean: ", type(bool(0)), bool(0), type(bool(1)), bool(1))


print("Преобразуйте False в строку: ", type(str(False)), str(False))