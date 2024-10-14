import json

from PyQt6.QtWidgets import QMessageBox

from MainWindow import Ui_MainWindow

class MainWindowEX(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.pushButtonSendData.clicked.connect(self.getInformation)
    def getInformation(self):
        fullName=self.lineEdit_name.text()
        email=self.lineEdit_email.text()
        gender="Woman"
        if not self.radioButton_man.isChecked():
            gender=self.radioButton_woman.text()
        address=self.lineEdit_address.text()
        degree="Bachelor"
        if self.radioButton_master.isChecked():
            degree=self.radioButton_master.text()
        elif self.radioButton_doctoral.isChecked():
            degree=self.radioButton_doctoral.text()
        information={"FullName":fullName,
                     "Email":email,
                     "Gender":gender,
                     "Address":address,
                     "Degree":degree
                     }
        self.msgBox=QMessageBox()
        self.msgBox.setWindowTitle("Information")
        self.msgBox.setText(json.dumps(information, ensure_ascii=False))
        self.msgBox.show()
    def show(self):
        self.MainWindow.show()