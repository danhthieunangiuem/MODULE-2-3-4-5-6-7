
from PyQt6.QtWidgets import QMessageBox

from MainWindow import Ui_MainWindow


class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.pushButton.clicked.connect(self.processSubmit)
    def show(self):
        self.MainWindow.show()
    def processSubmit(self):
        str=[]
        if self.checkBox_ml.isChecked()==True:
            str.append(self.checkBox_ml.text())
        if self.checkBox_dl.isChecked()==True:
            str.append(self.checkBox_dl.text())
        if self.checkBox_sc.isChecked()==True:
            str.append(self.checkBox_sc.text())

        separator=','
        full_name = self.lineEdit_name.text().strip()
        email = self.lineEdit_email.text().strip()

        # Kiểm tra nếu tên hoặc email bị để trống
        if not full_name or not email:
            self.msg = QMessageBox()
            self.msg.setWindowTitle("Error")
            self.msg.setText("Full Name and Email cannot be empty!")
            self.msg.setIcon(QMessageBox.Icon.Warning)
            self.msg.show()
            return

        # Kiểm tra nếu không có khóa học nào được chọn
        if not str:
            self.msg = QMessageBox()
            self.msg.setWindowTitle("Error")
            self.msg.setText("You must select at least one course!")
            self.msg.setIcon(QMessageBox.Icon.Warning)
            self.msg.show()
            return

        infor = "Full Name = " + self.lineEdit_name.text() + "\n"
        infor += "Email = " + self.lineEdit_email.text() + "\n"
        infor += "Selected courses:" + "\n"
        infor += separator.join(str)
        self.msg = QMessageBox()
        self.msg.setWindowTitle("Selected Courses")
        self.msg.setText(infor)

        self.msg.show()