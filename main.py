from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from myui import Ui_MainWindow
import sys
from combinatoric import Combinatoric

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        pixmap = QPixmap("img/sochetaniya.png")
        self.ui.label.setPixmap(pixmap)
        self.combinatoric = Combinatoric()
        self.ui.solve_button.clicked.connect(self.solve)
        self.ui.comboBox.currentIndexChanged.connect(self.setImg)
    
    def setImg(self):
        img = ["sochetaniya.png", "sochetaniya_with_repeat.png", "accomodattion_with_repeat.png"]
        selection = self.ui.comboBox.currentIndex()
        pixmap = QPixmap("img/" + img[selection])
        self.ui.label.setPixmap(pixmap)

    def solve(self):
        selection = self.ui.comboBox.currentIndex()
        n = self.ui.n_spinBox.value()
        m = self.ui.m_spinBox.value()
        if selection == 0 and n >= m:
            result = self.combinatoric.combinations_without_repeats(n, m)
        elif selection == 1:
            result = self.combinatoric.combinations_with_repeats(n, m)
        elif selection == 2:
            result = self.combinatoric.accommodation_with_repeats(n, m)
        else:
            result = "m должно быть меньше n"
        self.ui.result_lineEdit.setText(str(result))
 
if __name__ == '__main__': 
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()
    
    sys.exit(app.exec())
