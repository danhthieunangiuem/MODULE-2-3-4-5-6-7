from MainWindow import Ui_MainWindow


class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.pushButton.clicked.connect(self.Transfer)
    def Transfer(self):
        CAN = ["Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ", "Canh", "Tân", "Nhâm", "Quý"]
        CHI = ["Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"]
        nam=int(self.lineEdit.text())
        can = CAN[(nam+6) % 10]
        chi = CHI[(nam+8) % 12]
        kq=f'{can} {chi}'
        self.label_Lunar_tranfer.setText(str(kq))
    def show(self):
        self.MainWindow.show()