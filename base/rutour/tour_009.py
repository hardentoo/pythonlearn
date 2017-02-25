# http://python-rutour.rhcloud.com/tour/Files/

f = open('myfile.txt', 'r')  # Открываем в режиме чтения
text = f.read()  # Считываем
f.close()  # Закрываем файл
print(text)  # Выводим результат
f = open('myfile.txt', 'w')  # Открываем в режиме записи
f.write("Yo!")  # Записываем
f.close()  # Закрываем файл

# Использование менеджера контекста
# Менеджер контекста в любом случае закроет файл
with open("myfile.txt", 'w') as f:
    f.write("Yo!")
