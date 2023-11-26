import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from werkzeug.security import generate_password_hash, check_password_hash
from conex_db import database
from home import HomeWindow
from signup import SignScreen

con_db = database()
con_db.select_db()


class LoginScreen(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        screen_geometry = QApplication.primaryScreen().availableGeometry()
        window_width = 1000
        window_height = 800
        window_x = (screen_geometry.width() - window_width) // 2
        window_y = (screen_geometry.height() - window_height) // 2
        self.setGeometry(window_x, window_y, window_width, window_height)
        self.setObjectName("fondo")

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Crear un degradado de color para el fondo
        gradient = QLinearGradient(0, 0, self.width(), 0)
        gradient.setColorAt(0, QColor("#0e212c"))  # Color más claro a la izquierda
        gradient.setColorAt(0.5, QColor("#43423b"))  # Color más oscuro a la derecha
        gradient.setColorAt(1,QColor("#816d50"))
        # Establecer el degradado como fondo de la ventana
        palette = self.palette()
        palette.setBrush(QPalette.ColorGroup.All, QPalette.ColorRole.Window, QBrush(gradient))
        self.setPalette(palette)

        self.icon = QIcon

        self.tittle = QLabel("LOGIN", self)
        self.tittle.setGeometry(480, window_height // 2 - 250, 100, 30)
        self.tittle.setFont(QFont('vintage',20))

        self.username_label = QLabel("Username:", self)
        self.username_label.setGeometry(340, window_height // 2 - 200, 100, 30)
        self.username_label.setFont(QFont('Arial',12))

        self.username_input = QLineEdit(self)
        self.username_input.setGeometry(420, window_height // 2 - 200, 200, 30)

        self.username_feedback = QLabel("", self)
        self.username_feedback.setGeometry(
            430, window_height // 2 - 170, 300, 30)

        self.password_label = QLabel("Password:", self)
        self.password_label.setGeometry(340, window_height // 2 - 100, 100, 30)
        self.password_label.setFont(QFont('Arial',12))

        self.password_input = QLineEdit(self)
        self.password_input.setGeometry(420, window_height // 2 - 100, 200, 30)
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.password_feedback = QLabel("", self)
        self.password_feedback.setGeometry(
            430, window_height // 2 - 70, 300, 30)

        self.login_button = QPushButton("Login", self)
        self.login_button.setGeometry(440, window_height // 2 - 20, 120, 40)
        self.login_button.clicked.connect(self.login)
        self.login_button.setFont(QFont('Arial',10))
        
        self.close_button = QPushButton("X", self)
        self.close_button.clicked.connect(self.close)
        self.close_button.setGeometry(960, 0, 40, 40)

        self.minimize_button = QPushButton("-", self)
        self.minimize_button.clicked.connect(self.showMinimized)
        self.minimize_button.setGeometry(920, 0, 40, 40)

        self.register_button = QPushButton("Register Now", self)
        self.register_button.clicked.connect(self.red_register)
        self.register_button.setGeometry(440, window_height // 2 + 30, 120, 40)
        self.register_button.setFont(QFont('Arial',10))

        self.tittle.setStyleSheet("color:#251d1c;")
        self.username_label.setStyleSheet(" color:#816d50;")
        self.password_label.setStyleSheet(";color:#816d50;")

        self.login_button.setStyleSheet("background-color: #43423b;color:#d2c499;border-radius: 5px;")
        self.close_button.setStyleSheet("background-color: #fae9cc; color: white;")
        self.minimize_button.setStyleSheet("background-color: #d2c499; color: black;")
        self.register_button.setStyleSheet("background-color: #816d50;color:#122324; border-radius: 5px;")

    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
        self.dragPos = event.globalPosition().toPoint()
        event.accept()

        
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

    def red_register(self):
        print("Redireccioando")
        if not hasattr(self, 'register'):
            self.register = SignScreen()
            self.register.show()
            self.close()
        else:
            self.show()

    def paintEvent(self, event):
       # Pintar un cuadrado en la ventana
        painter = QPainter(self)

        # Definir el color original
        color_original = QColor("#b5b1a6")

        # Ajustar el brillo del color original para el fondo
        brillo_fondo = 150
        color_fondo = color_original.lighter(brillo_fondo)
        painter.fillRect(290, 100, 430, 430, color_fondo)

        # Ajustar el brillo del color original para el borde
        brillo_borde = 500
        color_borde = color_original.lighter(brillo_borde)

        # Dibujar un rectángulo más grande para el borde
        ancho_borde = 10
        painter.setPen(color_borde)  # Establecer el color del borde
        painter.drawRect(270, 90, 470, 470)

def main():
    app = QApplication(sys.argv)##administrar todo lo que se haga en la venta
    login_screen = LoginScreen()
    login_screen.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
