from MainWindow import Ui_MainWindow


class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.pushButton.clicked.connect(self.Convert)
    def Convert(self):
        Fahrenheit=float(self.lineEdit.text())
        Celsius = (Fahrenheit - 32) / 1.8
        Celsius=round(Celsius,2)
        self.labelC_kq.setText(str(Celsius))
    def show(self):
        self.MainWindow.show()