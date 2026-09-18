# todo: Единицы массы пронумерованы следующим образом: 1 — килограмм, 2 — миллиграмм, 3 — грамм,
# 4 — тонна, 5 — центнер. Дан номер единицы массы и масса тела M в этих единицах (вещественное число).
# Вывести массу данного тела в килограммах

import decimal
mass_converter = {1: 'килограмм', 2: 'миллиграмм', 3: 'грамм', 4: 'тонна', 5: 'центнер'}

# init_mass = 0
# result = 0

while True:
  init_mass = int(input('Введите единицу массы\n(1 — килограмм, 2 — миллиграмм, 3 — грамм, 4 — тонна, 5 — центнер): '))
  if 0 < init_mass < 6:
    break

body_mass = float(input("Введите массу тела в заданных единицах: "))


match init_mass:
  case 1:
    result = body_mass
  case 2:
    result = decimal.Decimal(str(body_mass)) / decimal.Decimal('1000000')
  case 3:
    result = decimal.Decimal(str(body_mass)) / decimal.Decimal('1000')
  case 4:
    result = body_mass * 1000
  case 5:
    result = body_mass * 100

print("Масса тела в килограммах: ", str(result))
