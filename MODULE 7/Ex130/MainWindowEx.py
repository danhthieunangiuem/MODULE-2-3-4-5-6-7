
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
import sys
from MainWindow import Ui_MainWindow

class MainWindowEx(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindowEx, self).__init__()
        self.setupUi(self)

        # Kết nối các nút với hàm xử lý
        self.pushButton_tinh.clicked.connect(self.tinh_khauhao)
        self.pushButton_xem.clicked.connect(self.xem_chitiet_khauhao)

    def tinh_khauhao(self):
        try:
            gia_mua = int(self.lineEdit_giamuamoi.text())
            phi_vanchuyen = int(self.lineEdit_phivanchuyen.text())
            chi_phi_lapdat = int(self.lineEdit_philapdat.text())
            so_nam = int(self.lineEdit_sonamsd.text())

            if gia_mua < 0 or phi_vanchuyen < 0 or chi_phi_lapdat < 0 or so_nam <= 0:
                raise ValueError("Các giá trị không được âm và số năm phải lớn hơn 0")

            nguyen_gia = gia_mua + phi_vanchuyen + chi_phi_lapdat
            khauhao_nam = nguyen_gia / so_nam
            khauhao_nam=round(khauhao_nam,2)
            khauhao_thang = khauhao_nam / 12
            khauhao_thang = round(khauhao_thang, 2)

            self.lineEdit_nguyengia.setText(str(nguyen_gia))
            self.lineEdit_khauhaonam.setText(str(khauhao_nam))
            self.lineEdit_khauhaothang.setText(str(khauhao_thang))
        except ValueError as ve:
            QMessageBox.warning(self, "Lỗi", f"Lỗi: {ve}")

    def xem_chitiet_khauhao(self):
        try:
            gia_mua = float(self.lineEdit_giamuamoi.text())
            phi_vanchuyen = float(self.lineEdit_phivanchuyen.text())
            chi_phi_lapdat = float(self.lineEdit_philapdat.text())
            so_nam = int(self.lineEdit_sonamsd.text())

            if gia_mua < 0 or phi_vanchuyen < 0 or chi_phi_lapdat < 0 or so_nam <= 0:
                raise ValueError("Các giá trị không được âm và số năm phải lớn hơn 0")

            nguyen_gia = gia_mua + phi_vanchuyen + chi_phi_lapdat
            khauhao_nam = nguyen_gia / so_nam

            chi_tiet = ""
            khauhao_luyke = 0

            for nam in range(1, so_nam + 1):
                if nam == so_nam:
                    khauhao_nam = nguyen_gia - khauhao_luyke
                khauhao_luyke += khauhao_nam
                chi_tiet += f"Năm {nam}: Còn lại: {nguyen_gia-khauhao_luyke:.2f}\n"

            self.textBrowser.setText(chi_tiet)
        except ValueError as ve:
            QMessageBox.warning(self, "Lỗi", f"Lỗi: {ve}")

