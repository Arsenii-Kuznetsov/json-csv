import csv
from docxtpl import DocxTemplate, R

filename = 'data_marathon.csv'
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
grouped_data = dict()
data_list.sort(key=lambda x: int(x[0]))
for marathon in data_list:
    year = marathon[0]
    name = marathon[1]
    gender = marathon[2]
    time = marathon[4]
    city = marathon[5]
    if year not in grouped_data:
        grouped_data[year] = dict()
    if city not in grouped_data[year]:
        grouped_data[year][city] = {'Male': ('', ''), 'Female': ('', '')}
    grouped_data[year][city][gender] = (name, time)
final_data = {}
for year, cities in grouped_data.items():
    final_data[year] = []
    for city, runners in cities.items():
        final_data[year].append({
            'city': city,
            'male_winner': runners['Male'][0],
            'male_time': runners['Male'][1],
            'female_winner': runners['Female'][0],
            'female_time': runners['Female'][1]
        })
doc = DocxTemplate('data_marathon.docx')
context = {
    'data': final_data,
    'page_break': R('\f')
}
doc.render(context)
doc.save('marathon.docx')
