# http://python-rutour.rhcloud.com/tour/Lists/

mylist = [1, 'два', 3.1]
print(len(mylist))  # Число элементов в списке
print(mylist[0])  # Доступ к первому элементу
mylist.append("new")
# Добавляем новый элемент в конец списка
print("Добавлен---->", mylist)
mylist.pop(0)  # Удаляем первый элемент
print("Удалён---->", mylist)  # Вложенные списки
superlist = [[1, 2, 3], [4, 5, 6]]
print(superlist)
print(superlist[1][1])  # Получаем 2 элемент во втором списке
