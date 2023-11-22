import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from werkzeug.security import generate_password_hash, check_password_hash
from conex_db import database

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
        self.password_feedback.setGeometry(380, 400, 300, 30)

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
        sql = "SELECT contraseña, rol FROM usuarios WHERE nombre_usuario = %s"
        con_db.cursor.execute(sql, (username,))  # type: ignore
        result = con_db.cursor.fetchone()  # type: ignore

        if result is None:
            print("Nombre de usuario incorrecto. Vuelve a intentarlo")
            self.username_feedback.setText(
                "Nombre de usuario incorrecto. Vuelve a intentarlo")
        else:
            hashed_password = result[0]
            role = result[1]
            if check_password_hash(hashed_password, password):

                if role == "admin":
                    print(username)
                    # print("¡Bienvenido administrador!")
                    # menu_home()  # Se pasa el valor de 'role' a la función menu_home()
                else:
                    print(username)
                    # menu_home()
                # Registrar en el historial
                # registrar_historial(f"Inicio de sesión", username)
                return True
            else:
                self.password_feedback.setText("Contraseña incorrecta.")
        return False


def main():
    app = QApplication(sys.argv)
    login_screen = LoginScreen()
    login_screen.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
