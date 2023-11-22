import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from werkzeug.security import generate_password_hash, check_password_hash
from conex_db import database
from home import HomeWindow

con_db = database()


class LoginScreen(QMainWindow):
    def __init__(self):
        super().__init__()

        # Remove window frame
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        # Calculate the position of the window in the center
        screen_geometry = QApplication.primaryScreen().availableGeometry()
        window_width = 1000
        window_height = 800
        window_x = (screen_geometry.width() - window_width) // 2
        window_y = (screen_geometry.height() - window_height) // 2
        self.setGeometry(window_x, window_y, window_width, window_height)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Create login form elements
        self.tittle = QLabel("LOGIN", self)
        self.tittle.setGeometry(480, 200, 100, 30)

        self.username_label = QLabel("Username:", self)
        self.username_label.setGeometry(380, 300, 100, 30)

        self.username_input = QLineEdit(self)
        self.username_input.setGeometry(460, 300, 200, 30)

        self.username_feedback = QLabel("", self)
        self.username_feedback.setGeometry(470, 330, 300, 30)

        self.password_label = QLabel("Password:", self)
        self.password_label.setGeometry(380, 370, 100, 30)

        self.password_input = QLineEdit(self)
        self.password_input.setGeometry(460, 370, 200, 30)
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.password_feedback = QLabel("", self)
        self.password_feedback.setGeometry(470, 400, 300, 30)

        self.login_button = QPushButton("Login", self)
        self.login_button.setGeometry(500, 500, 100, 30)
        self.login_button.clicked.connect(self.login)

        self.close_button = QPushButton("X", self)
        self.close_button.clicked.connect(self.close)
        self.close_button.setGeometry(960, 0, 40, 40)

        self.minimize_button = QPushButton("-", self)
        self.minimize_button.clicked.connect(self.showMinimized)
        self.minimize_button.setGeometry(920, 0, 40, 40)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        sql = "SELECT contrasenia, nombre FROM usuarios WHERE nombre = %s"
        con_db.cursor.execute(sql, (username,))
        result = con_db.cursor.fetchone()

        db_password = result[0]
        user = result[1]

        if result is None:
            print("Nombre de usuario incorrecto. Vuelve a intentarlo")
            self.username_feedback.setText(
                "Nombre de usuario incorrecto. Vuelve a intentarlo")
        else:
            if password == db_password:
                print("Bienvenido")
                self.username_feedback.setText("Usuario correcto")
                self.password_feedback.setText("Contraseña correcta")
                self.home_window = HomeWindow()
                self.home_window.show()
            else:
                self.password_feedback.setText("Contraseña incorrecta.")
                print("Acesso denegado")
        return False


def main():
    app = QApplication(sys.argv)
    login_screen = LoginScreen()

    login_screen.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
