import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *


class HomeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Home")
        screen_geometry = QApplication.primaryScreen().availableGeometry()
        window_width = 1000
        window_height = 800
        window_x = (screen_geometry.width() - window_width) // 2
        window_y = (screen_geometry.height() - window_height) // 2
        self.setGeometry(window_x, window_y, window_width, window_height)

        self.company_name = QLabel("VORTEX VENTURES", self)
        self.company_name.setGeometry(20, 30, 120, 20)
        self.create_navigation_bar()

    def create_navigation_bar(self):
        button_names = ["Button 1", "Button 2",
                        "Button 3", "Button 4", "Button 5", "Button 6"]
        navigation_bar = self.addToolBar("Navigation Bar")

        for name in button_names:
            button = QPushButton(name)
            button.clicked.connect(self.redirect_to_window)
            navigation_bar.addWidget(button)

    def redirect_to_window(self):
        # Logica para enviar a otras ventanas
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    home_window = HomeWindow()
    home_window.show()
    sys.exit(app.exec())
