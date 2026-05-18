import json

filename = 'animals.json'
try:
    with open(filename) as file:
        data = json.load(file)
except FileNotFoundError:
    exit(f"Файл '{filename}' не найден")
except PermissionError:
    exit(f"Нет прав на чтение файла '{filename}'")
except json.JSONDecodeError:
    exit(f"Файл содержит некорректный JSON.")
animals = data.get('animals')
if not animals:
    exit("Данные о животных отсутствуют")
birds = list(filter(lambda x: x.get('animal_type') == 'Bird', animals))
print('Птицы')
for bird in birds:
    for x in bird.items():
        print(f'{x[0]}: {x[1]}')
    print()
print(f"Количество дневных животных: {len(list(filter(lambda x: x.get('active_time') == 'Diurnal', animals)))}")
print('Животное с наименьшим весом')
animal = min(animals, key=lambda x: float(x.get("weight_min")) if x.get("weight_min") else float('inf'))
for x in animal.items():
    print(f'{x[0]}: {x[1]}')
