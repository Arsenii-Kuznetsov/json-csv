import csv

filename = 'countries.csv'
data_list = []
try:
    with open(filename, encoding='utf-8') as file:
        reader = csv.reader(file)
        try:
            data_list = list(reader)
        except UnicodeDecodeError:
            exit('Ошибка кодировки')
        except csv.Error:
            exit('Файл содержит некорректный CSV')
except FileNotFoundError:
    exit(f'Файл {filename} не найден')
except PermissionError:
    exit(f'Нет прав на чтение файла {filename}')
except IsADirectoryError:
    exit('Путь является папкой а не файлом')
if not data_list:
    exit('Файл пуст')
headers = ['Country', 'Health Care', 'Income', 'Inflation', 'Life Expectancy']
if [h.strip() for h in data_list[0]] != headers:
    exit('Некорректная структура файла')
try:
    min_income, max_income = map(float, input('Введите 2 числа диапазон доходов: ').split())
except ValueError:
    exit('Введены некорректные числа')
if max_income < 0 or min_income < 0 or min_income > max_income:
    exit('Диапазон указан неверно')
header_row = data_list[0]
rows = data_list[1:]
try:
    countries_specified_income = list(
        filter(lambda x: min_income <= float(x[2]) <= max_income, rows))
except ValueError:
    exit('В колонке Income содержатся не числа')
except IndexError:
    exit('Недостаточно колонок в файле')
with open('countries_specified_income.csv', 'w', newline='', encoding='utf-8') as file:
    file_writer = csv.writer(file)
    file_writer.writerow(header_row)
    file_writer.writerows(countries_specified_income)
try:
    countries_sorted_by_ihflation = sorted(rows, key=lambda x: float(x[3]))
except ValueError:
    exit('В колонке Inflation содержатся не числа')
except IndexError:
    exit('Недостаточно колонок в файле')
with open('countries_sorted_by_inflation.csv', 'w', newline='', encoding='utf-8') as file:
    file_writer = csv.writer(file)
    file_writer.writerow(header_row)
    file_writer.writerows(countries_sorted_by_ihflation)
