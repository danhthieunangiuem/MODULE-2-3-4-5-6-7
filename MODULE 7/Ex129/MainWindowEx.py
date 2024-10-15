from PyQt6.QtWidgets import QMessageBox

from MainWindow import Ui_MainWindow

class MainWindowExt(Ui_MainWindow):
    #override setupUi
    #just define attribute MainWindow for reuse in later
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.lineEdit_socu.textChanged.connect(self.updateSoKWh)
        self.lineEdit_somoi.textChanged.connect(self.updateSoKWh)
    #define methods for assigning Signals and Slots
    def processSignalAndSlot(self):
        self.pushButton_close.clicked.connect(self.processExit)
    #define slot exit window
    def processExit(self):
        dlg = QMessageBox(self.MainWindow)
        dlg.setWindowTitle("Exit Confirmation")
        dlg.setText("Are you sure you want to Exit?")
        dlg.setStandardButtons(
            QMessageBox.StandardButton.Yes
            | QMessageBox.StandardButton.No
        )
        dlg.setIcon(QMessageBox.Icon.Question)
        button = dlg.exec()
        # check the user confirmation
        button = QMessageBox.StandardButton(button)
        if button == QMessageBox.StandardButton.Yes:
            self.MainWindow.close()
        else:
            pass#do nothing

    def processSignalAndSlothd(self):
        self.pushButton_hd.clicked.connect(self.processHuongDan)

    def processHuongDan(self):
        dlg = QMessageBox(self.MainWindow)
        dlg.setWindowTitle("Thông báo")
        dlg.setText("Đây là phần mềm tính tiền điện\nKỹ sư thiết kế: Lê Hoài Thành Danh")
        dlg.setStandardButtons(
            QMessageBox.StandardButton.Ok
        )
        dlg.setIcon(QMessageBox.Icon.Question)
        button = dlg.exec()
        # check the user confirmation
        button = QMessageBox.StandardButton(button)
        if button == QMessageBox.StandardButton.Ok:
            pass  # do nothing

    def processSignalAndSlotTinhtiep(self):
        self.pushButton_tt.clicked.connect(self.processTinhtiep)

    def processTinhtiep(self):
        # Xóa trắng các ô nhập liệu
        self.lineEdit_socu.clear()
        self.lineEdit_somoi.clear()
        self.lineEdit_soho.clear()
        self.lineEdit_soKWh.clear()
        self.label_kqtienthu.clear()
        # Di chuyển con trỏ đến ô "Chỉ số cũ"
        self.lineEdit_socu.setFocus()

    def updateSoKWh(self):
        try:
            socu_text = self.lineEdit_socu.text()
            somoi_text = self.lineEdit_somoi.text()

            if socu_text == "" or somoi_text == "":
                self.lineEdit_soKWh.clear()  # Xóa nếu một trong hai trường nhập trống
                return

            socu = int(socu_text)
            somoi = int(somoi_text)

            # Kiểm tra giá trị âm
            if socu < 0 or somoi < 0:
                # Hiển thị thông báo lỗi nếu nhập giá trị âm
                dlg = QMessageBox(self.MainWindow)
                dlg.setWindowTitle("Lỗi nhập liệu")
                dlg.setText("Chỉ số cũ và chỉ số mới không được là số âm.")
                dlg.setIcon(QMessageBox.Icon.Warning)
                dlg.setStandardButtons(QMessageBox.StandardButton.Ok)
                dlg.exec()
                self.lineEdit_soKWh.clear()  # Xóa kết quả
                self.lineEdit_somoi.clear()
                self.lineEdit_socu.clear()
                self.lineEdit_socu.setFocus()
                return

            if socu > somoi :
                # Hiển thị thông báo lỗi nếu nhập giá trị âm
                dlg = QMessageBox(self.MainWindow)
                dlg.setWindowTitle("Lỗi nhập liệu")
                dlg.setText("Chỉ số cũ không được nhỏ hơn chỉ số mới.")
                dlg.setIcon(QMessageBox.Icon.Warning)
                dlg.setStandardButtons(QMessageBox.StandardButton.Ok)
                dlg.exec()
                self.lineEdit_soKWh.clear()  # Xóa kết quả
                self.lineEdit_somoi.clear()
                self.lineEdit_socu.clear()
                self.lineEdit_socu.setFocus()
                return

            # Tính số kWh nếu dữ liệu hợp lệ
            if somoi >= socu:
                sokwh = somoi - socu
                self.lineEdit_soKWh.setText(str(sokwh))  # Cập nhật vào ô kWh
            else:
                self.lineEdit_soKWh.setText("0")  # Trường hợp chỉ số mới nhỏ hơn chỉ số cũ
        except ValueError:
            # Nếu giá trị nhập không phải số, để ô kWh là trống
            self.lineEdit_soKWh.clear()

    def processSignalAndSlotSHBT(self):
        self.pushButton_SHBT.clicked.connect(self.processtinhGiaDienSHBT)

    def processtinhGiaDienSHBT(self):
        try:
            soho=int(self.lineEdit_soho.text())
            sokwh = int(self.lineEdit_soKWh.text())  # Lấy số kWh đã tính

            # Các mức giá điện sinh hoạt bậc thang
            bac1_gia = 1484
            bac2_gia = 1533
            bac3_gia = 1786
            bac4_gia = 2242
            bac5_gia = 2503
            bac6_gia = 2587

            # Tính chi phí điện theo từng bậc
            tong_tien = 0
            if sokwh <= 50:
                tong_tien = sokwh * bac1_gia
            elif sokwh <= 100:
                tong_tien = 50 * bac1_gia + (sokwh - 50) * bac2_gia
            elif sokwh <= 200:
                tong_tien = 50 * bac1_gia + 50 * bac2_gia + (sokwh - 100) * bac3_gia
            elif sokwh <= 300:
                tong_tien = 50 * bac1_gia + 50 * bac2_gia + 100 * bac3_gia + (sokwh - 200) * bac4_gia
            elif sokwh <= 400:
                tong_tien = 50 * bac1_gia + 50 * bac2_gia + 100 * bac3_gia + 100 * bac4_gia + (sokwh - 300) * bac5_gia
            else:
                tong_tien = 50 * bac1_gia + 50 * bac2_gia + 100 * bac3_gia + 100 * bac4_gia + 100 * bac5_gia + (
                            sokwh - 400) * bac6_gia

            # Cập nhật kết quả tính tiền điện
            self.label_kqtienthu.setText(f"Tiền SHBT: {tong_tien*soho} VND")

        except ValueError:
            self.label_kqtienthu.clear()  # Xóa nếu không tính được

    def processSignalAndSlotKd(self):
        self.pushButton_Kd.clicked.connect(self.processKd)

    def processKd(self):
        try:
            soho = int(self.lineEdit_soho.text())
            sokwh = int(self.lineEdit_soKWh.text())
            tong_tien=sokwh*2320
            self.label_kqtienthu.setText(f"Tiền điện Kinh doanh: {tong_tien * soho} VND")
        except ValueError:
            self.label_kqtienthu.clear()

    def processSignalAndSlotSX(self):
        self.pushButton_sx.clicked.connect(self.processSX)

    def processSX(self):
        try:
            soho = int(self.lineEdit_soho.text())
            sokwh = int(self.lineEdit_soKWh.text())
            tong_tien=sokwh*1518
            self.label_kqtienthu.setText(f"Tiền điện Sản xuất: {tong_tien * soho} VND")
        except ValueError:
            self.label_kqtienthu.clear()

    def show(self):
        self.MainWindow.show()