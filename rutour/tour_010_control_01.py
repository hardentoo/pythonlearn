# http://python-rutour.rhcloud.com/tour/Test_1/

# №1 Выведите из данного предложения только слово "друг"
mystr = "Привет, мой дорогой друг!"

print(mystr.split(' ')[3][:-1])

# №2 Выведите из данного списка только цифру 6
mylist = [1, 2, [18, 45, 87, [7, 6]]]

print(mylist[2][3][1])

# №3 Удалите цифру 2 в списке
mylist = [1, 2, 3, 4, 5, 6, 7]

mylist.pop(1)

print(mylist)

# №4 Выведите в одну строку имя и фамилию
mydic = {"name": "Иван", "surname": "Иванов", "age": 34}

print (mydic["name"] + ' ' +mydic["surname"])

'''№5 Сделайте из этих двух комментариев
один многострочный.'''

# №6 Экспериментируй и пробуй :)
