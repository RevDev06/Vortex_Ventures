import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


class LoginScreen(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pantalla de Inicio de Sesión")
        self.setGeometry(0, 0, 600, 400)

        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.center()
        self.dragging = False
        self.offset = QPoint()
        self.initLoginUI()

    def center(self):
        screen_geometry = QApplication.primaryScreen().availableGeometry()
        x = (screen_geometry.width() - self.width()) // 2
        y = (screen_geometry.height() - self.height()) // 2
        self.move(x, y)

    def initLoginUI(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Barra superior con botones
        self.title_bar = QFrame(self)
        self.title_bar.setFixedHeight(30)
        self.title_layout = QHBoxLayout(self.title_bar)

        home_button = QPushButton("Home")
        home_button.clicked.connect(self.showHome)

        close_button = QPushButton("Cerrar")
        close_button.clicked.connect(self.close)

        minimize_button = QPushButton("Minimizar")
        minimize_button.clicked.connect(self.showMinimized)

        self.title_layout.addWidget(home_button)
        self.title_layout.addWidget(close_button)
        self.title_layout.addWidget(minimize_button)

        # Resto de la interfaz de inicio de sesión
        layout = QVBoxLayout()
        label_username = QLabel("Nombre de usuario:")
        self.username_input = QLineEdit()

        label_password = QLabel("Contraseña:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        login_button = QPushButton("Iniciar Sesión")
        login_button.clicked.connect(self.login)

        layout.addWidget(self.title_bar)  # Agregar la barra superior
        layout.addWidget(label_username)
        layout.addWidget(self.username_input)
        layout.addWidget(label_password)
        layout.addWidget(self.password_input)
        layout.addWidget(login_button)

        central_widget.setLayout(layout)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if username == "usuario" and password == "contrasena":
            self.initHomeUI()
        else:
            print("Inicio de sesión fallido")

    def initHomeUI(self):
        home_tab = QTabWidget()
        self.setCentralWidget(home_tab)

        home_page = QTextEdit()
        home_page.setPlainText("Holi")

        home_tab.addTab(home_page, "Inicio")

    def showHome(self):
        self.initHomeUI()


def main():
    app = QApplication(sys.argv)
    login_screen = LoginScreen()
    login_screen.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
