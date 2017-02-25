# http://python-rutour.rhcloud.com/tour/Dicts/

mydic = {1: "Первый", 2: "Второй"}
print("Возьмём элемент с ключом 1 ------>", mydic[1])
superdic = {'name': {'first': 'Александр', 'second': 'Иванов'},
            'job': ['ОИТ', 'ОТК']}  # Более сложная структура
print(superdic['name']['second'], "--->", superdic['job'][0])
