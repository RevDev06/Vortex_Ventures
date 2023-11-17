import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


class LoginScreen(QMainWindow):
    def __init__(self):
        super().__init__()

        # Remove window frame
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        
        # Calculate the position of the window in the center
        screen_geometry = QApplication.primaryScreen().availableGeometry()
        window_width = 600
        window_height = 800
        window_x = (screen_geometry.width() - window_width) // 2
        window_y = (screen_geometry.height() - window_height) // 2
        self.setGeometry(window_x, window_y, window_width, window_height)


        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)



        self.close_button = QPushButton("Cerrar", self)
        self.close_button.clicked.connect(self.close)
        self.close_button.setGeometry(570, 10, 60, 30)

        minimize_button = QPushButton("Minimizar")
        minimize_button.clicked.connect(self.showMinimized)




def main():
    app = QApplication(sys.argv)
    login_screen = LoginScreen()
    login_screen.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
