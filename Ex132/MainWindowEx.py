from PyQt6.QtCore import Qt

from MainWindow import Ui_MainWindow


class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.checkBox_showhide.setChecked(True)
        self.checkBox_showhide.stateChanged.connect(self.processChecked)
    def show(self):
        self.MainWindow.show()
    def processChecked(self,value):
        state=Qt.CheckState(value)
        if state==Qt.CheckState.Checked:
            self.label.show()
        elif state==Qt.CheckState.Unchecked:
            self.label.hide()