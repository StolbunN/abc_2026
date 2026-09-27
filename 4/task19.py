#todo: Требуется создать csv-файл «algoritm.csv» со следующими столбцами:
# id) - номер по порядку (от 1 до 10);
# значение из списка algoritm

# algoritm = [ "C4.5" , "k - means" , "Метод опорных векторов" ,
#              "Apriori", "EM", "PageRank" , "AdaBoost", "kNN" ,
#              "Наивный байесовский классификатор", "CART" ]

# Каждое значение из списка должно находится на отдельной строке.
# Пример файла algoritm.csv:
# 1) "C4.5"
# 2) "k - means"
# .....
import csv

algoritm = [ "C4.5" , "k - means" , "Метод опорных векторов" ,
              "Apriori", "EM", "PageRank" , "AdaBoost", "kNN" ,
              "Наивный байесовский классификатор", "CART" ]

with open('algoritm.csv', mode='w', newline='', encoding='utf-8') as file:
  writer = csv.writer(file, delimiter=' ')
  for index, item in enumerate(algoritm):
    writer.writerow([f'{index + 1})', item])
