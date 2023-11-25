import sys
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

class Pag1(QWidget):
    def __init__(self):
        super(Pag1, self).__init__()

        self.nom_l = QLabel("Nombre del Puesto", self)
        self.nom_l.setGeometry(60,60, 120, 20)
        self.nom_t = QLineEdit(self)
        self.nom_t.setText('')
        self.nom_t.setGeometry(60,80, 800, 20)

        self.codp_l = QLabel("Codigo de Puesto", self)
        self.codp_l.setGeometry(60, 100, 100, 20)
        self.codp_t = QLineEdit(self)
        self.codp_t.setText('')
        self.codp_t.setGeometry(60,120, 400, 20)

        self.area_l=QLabel("Area de adscripcion", self)
        self.area_l.setGeometry(475,100, 150, 20)
        self.area_t=QLineEdit(self)
        self.area_t.setText('')
        self.area_t.setGeometry(475, 120, 385, 20)

        self.super_l=QLabel("Puesto del Jefe Superiro", self)
        self.super_l.setGeometry(60,140, 100, 20)
        self.super_t=QLineEdit(self)
        self.super_t.setText('')
        self.super_t.setGeometry(60,160, 800, 20)

        self.jornada_l=QLabel("Jornada", self)
        self.jornada_l.setGeometry(60,180, 100, 20)
        self.jornada_t=QLineEdit(self)
        self.jornada_t.setText('')
        self.jornada_t.setGeometry(60,200, 450, 20)

        self.remuneracion_l=QLabel("Remuneracion Mensual", self)
        self.remuneracion_l.setGeometry(530, 180, 200, 20)
        self.area_tremuneracion_t=QLineEdit(self)
        self.area_tremuneracion_t.setText('')
        self.area_tremuneracion_t.setGeometry(530, 200, 330, 20)

        self.prestaciones_l=QLabel("Presentaciones",self)
        self.prestaciones_l.setGeometry(60, 220, 800, 20)
        self.prestaciones_t=QLineEdit(self)
        self.prestaciones_t.setText('')
        self.prestaciones_t.setGeometry(60, 240, 800, 20)

        self.descripccion_l=QLabel("Descripcion General",self)
        self.descripccion_l.setGeometry(60,260, 150, 20)
        self.descripccion_t=QLineEdit(self)
        self.descripccion_t.setText('')
        self.descripccion_t.setGeometry(60,280, 800, 20)

        self.funciones_l=QLabel("Funciones", self)
        self.funciones_l.setGeometry(60, 300, 100, 20)
        self.funciones_t=QLineEdit(self)
        self.funciones_t.setText('')
        self.funciones_t.setGeometry(60, 320, 800, 20)

        self.edad_l=QLabel("Edad", self)
        self.edad_l.setGeometry(60, 340, 100, 20)
        self.edad_t=QLineEdit(self)
        self.edad_t.setText('')
        self.edad_t.setGeometry(60,360, 250, 20)

        self.sexo_l=QLabel("Sexo",self)
        self.sexo_l.setGeometry(340,340, 100, 20)
        self.sexo_t=QLineEdit(self)
        self.sexo_t.setText('')
        self.sexo_t.setGeometry(340,360, 250, 20)

        self.civil_l=QLabel("Estado Civi", self)
        self.civil_l.setGeometry(610,340, 150, 20)
        self.civil_t=QLineEdit(self)
        self.civil_t.setText('')
        self.civil_t.setGeometry(610,360, 250, 20)

        self.escolaridad_l=QLabel("Escolaridad", self)
        self.escolaridad_l.setGeometry(60,380, 150, 20)
        self.escolaridad_t=QLineEdit(self)
        self.escolaridad_t.setText('')
        self.escolaridad_t.setGeometry(60,400, 250, 20)

        self.gradoa_l=QLabel("Grado Avance", self)
        self.gradoa_l.setGeometry(340,380, 150, 20)
        self.gradoa_t=QLineEdit(self)
        self.gradoa_t.setText('')
        self.gradoa_t.setGeometry(340,400, 250, 20)

        self.carrera_l=QLabel("Carrera", self)
        self.carrera_l.setGeometry(610,380, 100, 20)
        self.carrera_t=QLineEdit(self)
        self.carrera_t.setText('')
        self.carrera_t.setGeometry(610,400, 250, 20)

##boton
        self.botona_pag = QPushButton("Continuar", self)
        self.botona_pag.setGeometry(400, 450, 70, 30)



class Pag2(QWidget):
    def __init__(self):
        super(Pag2, self).__init__()

       
        self.experiencia_l=QLabel("Experiencia", self)
        self.experiencia_l.setGeometry(60,60, 100, 20)
        self.experiencia_t=QLineEdit(self)
        self.experiencia_t.setText('')
        self.experiencia_t.setGeometry(60,80, 800, 20)

        self.conocimentos_l=QLabel("Conocimientos", self)
        self.conocimentos_l.setGeometry(60,100, 150, 20)
        self.conocimentos_t=QLineEdit(self)
        self.conocimentos_t.setText('')
        self.conocimentos_t.setGeometry(60,120, 800, 20)

        self.mequipo_l=QLabel("Manejo de Equipo",self)
        self.mequipo_l.setGeometry(60,140, 200, 20)
        self.mequipo_t=QLineEdit(self)
        self.mequipo_t.setText('')
        self.mequipo_t.setGeometry(60,160, 800, 20)

        self.rfisicos_l=QLabel("Requisitos Fisicos", self)
        self.rfisicos_l.setGeometry(60,180, 200, 20)
        self.rfisicos_t=QLineEdit(self)
        self.rfisicos_t.setText('')
        self.rfisicos_t.setGeometry(60, 200, 800, 20)

        self.rpsicologicos_l=QLabel("Requisitos Psicologicos", self)
        self.rpsicologicos_l.setGeometry(60, 220, 250, 20)
        self.rpsicologicos_t=QLineEdit(self)
        self.rpsicologicos_t.setText('')
        self.rpsicologicos_t.setGeometry(60, 240, 800, 20)

        self.responsabilidades_l=QLabel("Responsabilidades", self)
        self.responsabilidades_l.setGeometry(60 ,260, 200, 20)
        self.responsabilidades_t=QLineEdit(self)
        self.responsabilidades_t.setText('')
        self.responsabilidades_t.setGeometry(60,280, 800, 20)

        condiciones_l=QLabel("Condiciones de Trabajo", self)
        condiciones_l.setGeometry(60,300, 300, 20)
        condiciones_t=QLineEdit(self)
        condiciones_t.setText('')
        condiciones_t.setGeometry(60, 320, 800, 20)

        self.idiomas_l=QLabel("Idiomas", self)
        self.idiomas_l.setGeometry(60,340, 100, 20)
        self.idiomast_t=QLineEdit(self)
        self.idiomast_t.setText('')
        self.idiomast_t.setGeometry(60,360, 385, 20)

        self.habilidades_l=QLabel("Habilidades", self)
        self.habilidades_l.setGeometry(475, 340, 150, 20)
        self.habilidades_t=QLineEdit(self)
        self.habilidades_t.setText('')
        self.habilidades_t.setGeometry(475,360, 385, 20)

#Boton
        self.botona_pag=QPushButton("Guardar y Regresar", self)
        self.botona_pag.setGeometry(400, 400, 120, 30)

class aplicacion(QMainWindow):
    def __init__(self):
        super(aplicacion, self).__init__()

        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        self.aplicacion_widgets=QStackedWidget(self)
        self.pag_1= Pag1()
        self.pag_2= Pag2()
        self.aplicacion_widgets.addWidget(self.pag_1)
        self.aplicacion_widgets.addWidget(self.pag_2)
        self.setCentralWidget(self.aplicacion_widgets)
        self.aplicacion_widgets.setCurrentWidget(self.pag_1)
        self.inicializar_ui()
        
        self.close_button = QPushButton("X", self)
        self.close_button.clicked.connect(self.close)
        self.close_button.setGeometry(960, 0, 40, 40)

        self.minimize_button = QPushButton("-", self)
        self.minimize_button.clicked.connect(self.showMinimized)
        self.minimize_button.setGeometry(920, 0, 40, 40)
        
    def inicializar_ui(self):
        self.resize(1000,600)
        self.setWindowTitle('Detalles del Puesto')
        self.conexiones()

    def conexiones(self):
        self.pag_1.botona_pag.clicked.connect(self.cambio_pag_2)
        self.pag_2.botona_pag.clicked.connect(self.cambio_pag_1)

    def cambio_pag_2(self):
        self.aplicacion_widgets.setCurrentWidget(self.pag_2)

    def cambio_pag_1(self):
        self.aplicacion_widgets.setCurrentWidget(self.pag_1)

if __name__ == '__main__':
    with open('styles.css', 'r') as f:
        style = f.read()
    app = QApplication(sys.argv)##administrar todo lo que se haga en la venta
    app.setStyleSheet(style)  # Aplicar el estilo global
    ventana=aplicacion()
    ventana.show()
    sys.exit(app.exec())
