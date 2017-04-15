# http://python-rutour.rhcloud.com/tour/Strings/

line = "Это строка"
print(line)
print("Длина строки: ", len(line))
print(line[0])  # Первый элемент, счёт начинается с нуля
print(line[1])  # Второй элемент
print(line[-1])  # Последний элемент
print(line[1:4])  # Срез
print(line[:4])  # Тоже срез
print(line[4:])  # Ещё вариант
print(line + line)  # Прибавляем строку к строке
print(line * 3)  # Так тоже можно
