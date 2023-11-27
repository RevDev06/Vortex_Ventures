from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import sys
from test_db import TestDatabase

class Window(QWidget):
    def __init__(self):
        super().__init__()
        # Remove window frame
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        # Calculate the position of the window in the center
        screen_geometry = QApplication.primaryScreen().availableGeometry()
        window_width = 350
        window_height = 150
        window_x = (screen_geometry.width() - window_width) // 2
        window_y = (screen_geometry.height() - window_height) // 2
        self.setGeometry(window_x, window_y, window_width, window_height)
        self.setStyleSheet("background-color: #161616")

        self.prog_bar = QProgressBar(self)
        self.prog_bar.setGeometry(40, 70, 270, 40)
        
        self.company_name = QLabel(self)
        self.company_name.setText("VORTEX VENTURES")
        self.company_name.setObjectName("company_name")
        self.company_name.setGeometry(40, 20, 180, 20)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.auto_increment)
        self.timer.start(300)  # auto-increment every 1000 milliseconds

        self.close_button = QPushButton("X", self)
        self.close_button.clicked.connect(self.close)
        self.close_button.setGeometry(300, 10, 40, 40)

        self.minimize_button = QPushButton("-", self)
        self.minimize_button.setObjectName("minimize_button")
        self.minimize_button.clicked.connect(self.showMinimized)
        self.minimize_button.setGeometry(260, 10, 40, 40)

    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
        self.dragPos = event.globalPosition().toPoint()
        event.accept()

    def auto_increment(self):
        value = self.prog_bar.value()
        self.prog_bar.setValue(0)
        if self.run_tests():
            self.prog_bar.setValue(value + 2)
        if self.prog_bar.value() == 100 or self.prog_bar.value() == 99:
            self.timer.stop()
            self.red_login()

    def run_tests(self):
        # Run your tests here
        # Return True if tests pass, False otherwise
        test_db = TestDatabase()
        test_db.setUp()
        test_db.test_init()
        test_db.test_close_conex()
        test_db.test_comit()
        test_db.test_select_db()
        return True

    def red_login(self):
        from login import LoginScreen
        print("Redireccioando")
        if not hasattr(self, 'login'):
            self.login = LoginScreen()
            self.login.show()
            self.close()
        else:
            self.show()

if __name__ == '__main__':
    with open('styles.css', 'r') as f:
        style = f.read()
    app = QApplication(sys.argv)##administrar todo lo que se haga en la venta
    app.setStyleSheet(style)
    ventana = Window()
    ventana.show()
    sys.exit(app.exec())
