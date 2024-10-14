from PyQt6.QtWidgets import QApplication, QMainWindow
import sys
from MainWindowEx import MainWindowEx

def main():
    # Tạo đối tượng ứng dụng PyQt
    app = QApplication(sys.argv)

    # Tạo cửa sổ chính
    window = MainWindowEx()

    # Hiển thị cửa sổ
    window.show()

    # Khởi động vòng lặp sự kiện
    sys.exit(app.exec())

if __name__ == "__main__":
    main()