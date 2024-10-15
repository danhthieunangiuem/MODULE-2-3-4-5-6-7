from PyQt6.QtWidgets import QApplication, QMainWindow,QMessageBox

from MainWindowEx import MainWindowExt

#Create QApplication instance
app=QApplication([])
#Create QMainWindow instance
qMainWindow=QMainWindow()
#Create MyQMainWindowExt instance
myWindow=MainWindowExt()
#call setupUi method for MyQMainWindowExt
myWindow.setupUi(qMainWindow)
#call methods for Signal and slots processing
myWindow.processSignalAndSlot()
myWindow.processSignalAndSlothd()
myWindow.processSignalAndSlotTinhtiep()
myWindow.processSignalAndSlotSHBT()
myWindow.processSignalAndSlotKd()
myWindow.processSignalAndSlotSX()
#call show method to show Window
qMainWindow.show()
#start Event loop
app.exec()