from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QMovie

from MainWindow import Ui_MainWindow


class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        #change text
        self.pushButton_change.clicked.connect(self.processChangeText)
        #change font
        self.pushButton_font.clicked.connect(self.processChangeFontSize)
        #set align text
        self.pushButton_left.clicked.connect(self.processAlignLeft)
        self.pushButton_center.clicked.connect(self.processAlignCenter)
        self.pushButton_right.clicked.connect(self.processAlignRight)
        #change image with PNG format
        self.pushButton_png.clicked.connect(self.processChangePNG)
        #change image with gif format
        self.pushButton_if.clicked.connect(self.processChangeGIF)
    def show(self):
        self.MainWindow.show()
    def processChangeText(self):
        self.Titlelabel.setText("https://www.facebook.com/danhloptruong")
    def processChangeFontSize(self):
        #get font object
        font=self.Titlelabel.font()
        #change font size
        font.setPointSize(20)
        #set italic
        font.setItalic(True)
        #set bold
        font.setBold(True)
        #set font name
        font.setFamily("cambria")
        #re-assign font
        self.Titlelabel.setFont(font)
    def processAlignLeft(self):
        self.Titlelabel.setAlignment(Qt.AlignmentFlag.AlignLeft)
    def processAlignCenter(self):
        self.Titlelabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
    def processAlignRight(self):
        self.Titlelabel.setAlignment(Qt.AlignmentFlag.AlignRight)
    def processChangePNG(self):
        #create QPixmap instance
        pixmap=QPixmap("images/image1.jpg")
        #set pixmap for label
        self.label_image.setPixmap(pixmap)
    def processChangeGIF(self):
        #create QMovie instance
        movie=QMovie("images/image2.gif")
        #set movie object for label
        self.label_image.setMovie(movie)
        #call start method
        movie.start()