import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from werkzeug.security import generate_password_hash, check_password_hash
from conex_db import database
from login import LoginScreen


con_db = database()
con_db.verifAndCreateDataBase()
con_db.select_db()


class SignScreen(QMainWindow):
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
         # Create login form elements
        self.tittle = QLabel("SIGN UP", self)
        self.tittle.setGeometry(window_width // 2 - 50, 150, 220, 80)
        self.tittle.setFont(QFont("vintage", 20))

        self.username_label = QLabel("Username:", self)
        self.username_label.setGeometry(380, 300, 100, 30)
        self.username_label.setFont(QFont('Arial',12))

        self.username_input = QLineEdit(self)
        self.username_input.setGeometry(460, 300, 200, 30)

        self.username_feedback = QLabel("", self)
        self.username_feedback.setGeometry(470, 330, 300, 30)

        self.email_label = QLabel("Email:", self)
        self.email_label.setGeometry(380, 370, 100, 30)
        self.email_label.setFont(QFont('Arial',12))

        self.email_input = QLineEdit(self)
        self.email_input.setGeometry(460, 370, 200, 30)

        self.email_feedback = QLabel("", self)
        self.email_feedback.setGeometry(470, 400, 300, 30)

        self.password_label = QLabel("Password:", self)
        self.password_label.setGeometry(380, 440, 100, 30)
        self.password_label.setFont(QFont('Arial',12))

        self.password_input = QLineEdit(self)
        self.password_input.setGeometry(460, 440, 200, 30)
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.password_feedback = QLabel("", self)
        self.password_feedback.setGeometry(470, 470, 300, 30)

##Guardado de cuenta
        self.sign_button = QPushButton("Sign up", self)
        self.sign_button.setGeometry(window_width // 2 - 60, window_height // 2 + 100, 120, 40)
        self.sign_button.clicked.connect(self.signUp)
        self.sign_button.setFont(QFont('Arial',10))


        self.back_button = QPushButton("Back to Login", self)
        self.back_button.setGeometry(window_width // 2 - 60, window_height // 2 + 160, 120, 40)
        self.back_button.clicked.connect(self.vuelve)
        self.back_button.setFont(QFont('Arial',10))

        self.close_button = QPushButton("X", self)
        self.close_button.clicked.connect(self.close)
        self.close_button.setGeometry(960, 0, 40, 40)
        self.close_button.setStyleSheet("background-color:#5f5a4d; color:#ccc6ac;border-radius: 5px;")


        self.minimize_button = QPushButton("-", self)
        self.minimize_button.clicked.connect(self.showMinimized)
        self.minimize_button.setGeometry(920, 0, 40, 40)
        self.minimize_button.setStyleSheet("background-color:#867c61; color:#ccc6ac;border-radius: 5px;")

        self.tittle.setStyleSheet("color:#251d1c;")
        self.username_label.setStyleSheet(" color:#816d50;")
        self.email_label.setStyleSheet(" color:#816d50;")
        self.password_label.setStyleSheet(";color:#816d50;")

        self.sign_button.setStyleSheet("background-color: #43423b;color:#d2c499;border-radius: 5px;")
    
        self.back_button.setStyleSheet("background-color: #816d50;color:#122324; border-radius: 5px;")

    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
        self.dragPos = event.globalPosition().toPoint()
        event.accept()


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
                else:
                    print("Email valido")
                    sql = "INSERT INTO usuarios (nombre, correo, contrasenia) VALUES (%s, %s, %s)"
                    values = (username, email, password)
                    con_db.cursor.execute(sql, values)
                    con_db.comit()
                    #Se indica si el registro fue exitoso
                    print("Usuario registrado correctamente.")
                    self.username_feedback.setText("Usuario guardado")
                    self.email_feedback.setText("Email guardado")
                    self.password_feedback.setText("Contraseña guardada")
                    break

        else:
            print("Nombre de usuario ya se esta usando. Vuelve a intentarlo")
            self.username_feedback.setText(
                "Nombre de usuario ya se esta usando. Vuelve a intentarlo")
        return False
    
    def vuelve(self):
        from login import LoginScreen
        print("Redireccioando")
        if not hasattr(self, 'login'):
            self.login = LoginScreen()
            self.login.show()
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
        painter.fillRect(290, 130, 430, 500, color_fondo)

        # Ajustar el brillo del color original para el borde
        brillo_borde = 500
        color_borde = color_original.lighter(brillo_borde)

        # Dibujar un rectángulo más grande para el borde
        ancho_borde = 10
        painter.setPen(color_borde)  # Establecer el color del borde
        painter.drawRect(270, 110, 470, 540)

def main():
    app = QApplication(sys.argv)##administrar todo lo que se haga en la venta
    with open('styles.css', 'r') as f:
        style = f.read()
    app.setStyleSheet(style)
    signscreen = SignScreen()
    signscreen.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
