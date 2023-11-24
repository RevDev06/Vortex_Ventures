import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from werkzeug.security import generate_password_hash, check_password_hash
from conex_db import database

con_db = database()


class SignScreen(QMainWindow):
    def __init__(self):
        super().__init__()

        # Remove window frame
        ##self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        # Calculate the position of the window in the center
        screen_geometry = QApplication.primaryScreen().availableGeometry()
        window_width = 1000
        window_height = 800
        window_x = (screen_geometry.width() - window_width) // 2
        window_y = (screen_geometry.height() - window_height) // 2
        self.setGeometry(window_x, window_y, window_width, window_height)
        self.setObjectName("fondo")

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Create sign form elements
         # Create login form elements
        self.tittle = QLabel("SIGN UP", self)
        self.tittle.setGeometry(480, 200, 100, 30)

        self.username_label = QLabel("Username:", self)
        self.username_label.setGeometry(380, 300, 100, 30)

        self.username_input = QLineEdit(self)
        self.username_input.setGeometry(460, 300, 200, 30)

        self.username_feedback = QLabel("", self)
        self.username_feedback.setGeometry(470, 330, 300, 30)
##mio
        self.email_label = QLabel("Email:", self)
        self.email_label.setGeometry(380, 370, 100, 30)

        self.email_input = QLineEdit(self)
        self.email_input.setGeometry(460, 370, 200, 30)

        self.email_feedback = QLabel("", self)
        self.email_feedback.setGeometry(470, 400, 300, 30)
##mio
        self.password_label = QLabel("Password:", self)
        self.password_label.setGeometry(380, 440, 100, 30)

        self.password_input = QLineEdit(self)
        self.password_input.setGeometry(460, 440, 200, 30)
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.password_feedback = QLabel("", self)
        self.password_feedback.setGeometry(470, 470, 300, 30)

##Guardado de cuenta
        self.sign_button = QPushButton("Sign up", self)
        self.sign_button.setGeometry(445, 500, 100, 30)
        self.sign_button.clicked.connect(self.signUp)

        self.sign_button = QPushButton("Back to Login", self)
        self.sign_button.setGeometry(445, 540, 100, 30)
        self.sign_button.clicked.connect(self.signUp)

        self.close_button = QPushButton("X", self)
        self.close_button.clicked.connect(self.close)
        self.close_button.setGeometry(960, 0, 40, 40)

        self.minimize_button = QPushButton("-", self)
        self.minimize_button.clicked.connect(self.showMinimized)
        self.minimize_button.setGeometry(920, 0, 40, 40)

    def signUp(self):
        username = self.username_input.text()
        email = self.email_input.text()
        password = self.password_input.text()
        sql = "SELECT contrasenia, nombre FROM usuarios WHERE nombre = %s"
        con_db.cursor.execute(sql, (username,))
        result = con_db.cursor.fetchone()

        if result is None:
            print("Registrando")
            ##La conrtaseña se carga en la db
            for a in email:
                if a != "@":
                    print("Email invalido")
                    self.email_feedback.setText("Email invalido")
                    break
                else:
                    print("Email valido")
                    sql = "INSERT INTO usuarios (nombre, correo, contrasenia) VALUES (%s, %s, %s)"
                    values = (username, email, password)
                    con_db.cursor.execute(sql, values)
                    #Se indica si el registro fue exitoso
                    print("Usuario registrado correctamente.")
                    self.username_feedback.setText("Usuario guardado")
                    self.email_feedback.setText("Email guardado")
                    self.password_feedback.setText("Contraseña guardada")
        else:
            print("Nombre de usuario ya se esta usando. Vuelve a intentarlo")
            self.username_feedback.setText(
                "Nombre de usuario ya se esta usando. Vuelve a intentarlo")
        return False


def main():
    with open('styles.css', 'r') as f:
        style = f.read()
    app = QApplication(sys.argv)##administrar todo lo que se haga en la venta
    app.setStyleSheet(style)  # Aplicar el estilo global
    signscreen = SignScreen()
    signscreen.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
