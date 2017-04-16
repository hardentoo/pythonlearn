import sys
from check import *
from PyQt5 import QtCore, QtGui, QtWidgets

# Импортируем модули нужные для проверки доменов
import whois
import re

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Этой строчкой мы вешаем на кнопку нашу новую функцию
        # под названием DomainCheck
        self.ui.pushButton.clicked.connect(self.DomainCheck)

    # Собственно описываем функцию DomainCheck
    # которая вызывается при нажатии кнопки
    def DomainCheck(self):
        # Очищаем текстовое поле с результатами
        self.ui.textEdit_2.setText("")
        # В переменную stroki получаем текст из левого поля ввода
        stroki=self.ui.textEdit.toPlainText()
        # Получаем массив строк разделив текст по знаку переноса строки
        mas=stroki.split('\n')
        # Обнуляем переменную где будут копиться свободные домены
        rezultat='';
        # Выводим надпись чтобы пользователь подождал
        self.ui.textEdit_2.setText("Пожалуйста ждите, идет проверка!")
        # Перебираем массив строчек с названиями доменов
        for stroka in mas:
            # В переменную domain кладем очищенное от лишних символов имя домена
            domain = re.sub("^\s+|\n|\r|\s+$", '', stroka)
            # Проверяем свободно ли данное доменное имя
            m = whois.whois(domain)
            # Если свободно то добавляем его в rezultat
            if(m.status==None):
                rezultat=rezultat+domain+'\n'
        # Выводим в правое поле переменную rezultat со списком свободных доменов
        self.ui.textEdit_2.setText(rezultat)

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
