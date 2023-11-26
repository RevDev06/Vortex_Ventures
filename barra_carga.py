from PyQt6.QtWidgets import QApplication, QWidget, QProgressBar, QPushButton, QVBoxLayout
from PyQt6.QtCore import QTimer, Qt
import sys


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
        self.prog_bar.setGeometry(50, 50, 250, 30)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.auto_increment)
        self.timer.start(500)  # auto-increment every 1000 milliseconds

        self.close_button = QPushButton("X", self)
        self.close_button.clicked.connect(self.close)
        self.close_button.setGeometry(250, 10, 60, 30)

        self.minimize_button = QPushButton("-", self)
        self.minimize_button.setObjectName("minimize_button")
        self.minimize_button.clicked.connect(self.showMinimized)
        self.minimize_button.setGeometry(180, 10, 60, 30)

    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
        self.dragPos = event.globalPosition().toPoint()
        event.accept()

    def auto_increment(self):
        value = self.prog_bar.value()
        self.prog_bar.setValue(value + 1)


if __name__ == '__main__':
    with open('styles.css', 'r') as f:
        style = f.read()
    app = QApplication(sys.argv)##administrar todo lo que se haga en la venta
    app.setStyleSheet(style)
    ventana = Window()
    ventana.show()
    sys.exit(app.exec())
