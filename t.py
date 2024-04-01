import json

# Чтение файла namaz.json
with open('apps/education/fixtures/images4.json', 'r') as file:
    data = json.load(file)


# Изменение значений
for i, item in enumerate(data, start=1):
    item["pk"] += 43
    item["fields"]["namaz"] += 38

# Запись измененных данных обратно в файл
with open('apps/education/fixtures/images5.json', 'w') as file:
    json.dump(data, file, indent=4)
