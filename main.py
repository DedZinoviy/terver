from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from myui import Ui_MainWindow
import sys
from combinatoric import Combinatoric

class mywindow(QtWidgets.QMainWindow):

    '''Конструктор главного окна'''
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Установить формулу по-умолчанию
        pixmap = QPixmap("img/sochetaniya.png")
        self.ui.formula_img.setPixmap(pixmap)

        # Установить коннекты
        self.ui.solve_button.clicked.connect(self.solve)
        self.ui.comboBox.currentIndexChanged.connect(self.setImg)
    
    '''Изменить изображение формулы'''
    def setImg(self):
        img = ["sochetaniya.png", "sochetaniya_with_repeat.png", "accomodattion_with_repeat.png"]
        selection = self.ui.comboBox.currentIndex()
        pixmap = QPixmap("img/" + img[selection])
        self.ui.formula_img.setPixmap(pixmap)

    '''Произвести расчет выбранной формулы'''
    def solve(self):
        # Считать введенные данные
        selection = self.ui.comboBox.currentIndex()
        n = self.ui.n_spinBox.value()
        m = self.ui.m_spinBox.value()

        # В зависимости от выбранной формулы произвести вычисления
        if selection == 0 and n >= m:
            result = Combinatoric.combinations_without_repeats(n, m)
        elif selection == 1:
            result = Combinatoric.combinations_with_repeats(n, m)
        elif selection == 2:
            result = Combinatoric.accommodation_with_repeats(n, m)
        else:
            result = "m должно быть меньше n"

        # Вывести полученное значение в поле ответа
        self.ui.result_textEdit.setText(str(result))

# Запуск главного окна 
if __name__ == '__main__': 
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()
    
    sys.exit(app.exec())
