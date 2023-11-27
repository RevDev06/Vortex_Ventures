import sys
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *

class vpuesto(QWidget):
    def __init__(self):
        super(vpuesto, self).__init__()
        self.fila = 0
        self.columna = 2
        self.generartabla()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        screen_geometry = QApplication.primaryScreen().availableGeometry()
        window_width = 1000
        window_height = 800
        window_x = (screen_geometry.width() - window_width) // 2
        window_y = (screen_geometry.height() - window_height) // 2
        self.setGeometry(window_x, window_y, window_width, window_height)

    def generartabla(self):
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(self.fila)
        self.tableWidget.setColumnCount(self.columna) 
        # Configuración adicional
        column_width = 490
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        for i in range(self.columna):
            self.tableWidget.setColumnWidth(i, column_width)

        self.agregar = QPushButton('Agregar candidato')
        self.agregar.setFixedSize(140, 30)

        self.detalles=QPushButton('Detalles')
        self.detalles.setFixedSize(100, 30)

        self.editar = QPushButton('Editar')
        self.editar.setFixedSize(100, 30)

        blayout = QHBoxLayout()
        blayout.addWidget(self.agregar)
        blayout.addWidget(self.detalles)
        blayout.addWidget(self.editar)

        layout = QVBoxLayout(self)
        layout.addLayout(blayout)
        layout.addWidget(self.tableWidget)

    def obtener_filas(self):
        return self.fila

    def agregar_fila(self, nombre):
        self.fila += 1
        self.tableWidget.setRowCount(self.fila)

        puesto = QLabel(f'{nombre}')
        puesto.setAlignment(Qt.AlignmentFlag.AlignCenter)           
        self.tableWidget.setCellWidget(self.fila - 1, 0, puesto)

        borrar = QPushButton('Borrar')
        self.tableWidget.setCellWidget(self.fila - 1, 1, borrar)
        borrar.clicked.connect(self.borra)

    def borra(self):
        index = self.tableWidget.indexAt(self.sender().pos())
        if index.isValid():
            fila = index.row()
            self.tableWidget.removeRow(fila)
            self.fila -= 1   

    def borrar_cancelar(self):
        if self.fila > 0:
            self.fila -= 1
            self.tableWidget.setRowCount(self.fila)

class agregacandidato1(QWidget):
    def __init__(self):
        super(agregacandidato1, self).__init__()
        self.id_l = QLabel("Id", self)
        self.id_l.setGeometry(60,60, 120, 20)
        self.id_t = QLineEdit(self)
        self.id_t.setGeometry(60,80, 95, 20)

        self.nom_l = QLabel("Nombre", self)
        self.nom_l.setGeometry(165,60, 120, 20)
        self.nom_t = QLineEdit(self)
        self.nom_t.setGeometry(165,80, 800, 20)

        self.apeM_l = QLabel("Apellido Materno", self)
        self.apeM_l.setGeometry(60, 100, 100, 20)
        self.apeM_t = QLineEdit(self)
        self.apeM_t.setGeometry(60,120, 410, 20)

        self.apeP_l=QLabel("Apellido Paterno", self)
        self.apeP_l.setGeometry(480,100, 150, 20)
        self.apeP_t=QLineEdit(self)
        self.apeP_t.setGeometry(480, 120, 485, 20)

        self.telefono_l=QLabel("Numero de Telefono", self)
        self.telefono_l.setGeometry(60,140, 100, 20)
        self.telefono_t=QLineEdit(self)
        self.telefono_t.setGeometry(60,160, 750, 20)

        self.edad_l=QLabel('Edad', self)
        self.edad_l.setGeometry(817,140, 100, 20)
        self.edad_t=QLineEdit(self)
        self.edad_t.setGeometry(820,160, 145, 20)

        self.correo_l=QLabel('Correo Electronico', self)
        self.correo_l.setGeometry(60,180, 100, 20)
        self.correo_t=QLineEdit(self)
        self.correo_t.setGeometry(60,200, 905, 20)

        self.direccion_l=QLabel('Direccion', self)
        self.direccion_l.setGeometry(60,220, 100, 20)
        self.direccion_t=QLineEdit(self)
        self.direccion_t.setGeometry(60,240, 905, 20)

        self.puesto_l = QLabel("Puesto", self)
        self.puesto_l.setGeometry(60, 260, 100, 20)
        self.puesto_t = QLineEdit(self)
        self.puesto_t.setGeometry(60,280, 410, 20)

        self.carrera_l=QLabel("Carrera", self)
        self.carrera_l.setGeometry(480,260, 150, 20)
        self.carrera_t=QLineEdit(self)
        self.carrera_t.setGeometry(480, 280, 485, 20)

        self.gradoava_l = QLabel("Grado Avance", self)
        self.gradoava_l.setGeometry(60, 300, 100, 20)
        self.gradoava_t = QLineEdit(self)
        self.gradoava_t.setGeometry(60,320, 425, 20)

        self.estadociv_l=QLabel("Estado Civil", self)
        self.estadociv_l.setGeometry(495,300, 150, 20)
        self.estadociv_t=QLineEdit(self)
        self.estadociv_t.setGeometry(495, 320, 468, 20)

        self.escolaridad_l = QLabel("Escolaridad", self)
        self.escolaridad_l.setGeometry(60, 340, 100, 20)
        self.escolaridad_t = QLineEdit(self)
        self.escolaridad_t.setGeometry(60,360, 400, 20)

        self.sexo_l=QLabel("Sexo", self)
        self.sexo_l.setGeometry(470,340, 150, 20)
        self.sexo_t=QLineEdit(self)
        self.sexo_t.setGeometry(470, 360, 493, 20)

        self.habili_l=QLabel('Habilidades', self)
        self.habili_l.setGeometry(60,380, 100, 20)
        self.habili_t=QLineEdit(self)
        self.habili_t.setGeometry(60,400, 905, 20)

        self.botona_pag=QPushButton("Continuar", self)
        self.botona_pag.setGeometry(150, 450, 80, 30)

        self.botoncancelar=QPushButton("Cancelar", self)
        self.botoncancelar.setGeometry(60, 450, 70, 30)

    def limpiar(self):
        for child_widget in self.findChildren(QLineEdit):
            child_widget.clear()

class ventanaedit(QWidget):
    def __init__(self):
        super(ventanaedit, self).__init__()
        self.id_l = QLabel("Id", self)
        self.id_l.setGeometry(60,60, 120, 20)
        self.id_t = QLineEdit(self)
        self.id_t.setGeometry(60,80, 95, 20)

        self.nom_l = QLabel("Nombre", self)
        self.nom_l.setGeometry(165,60, 120, 20)
        self.nom_t = QLineEdit(self)
        self.nom_t.setGeometry(165,80, 800, 20)

        self.apeM_l = QLabel("Apellido Materno", self)
        self.apeM_l.setGeometry(60, 100, 100, 20)
        self.apeM_t = QLineEdit(self)
        self.apeM_t.setGeometry(60,120, 410, 20)

        self.apeP_l=QLabel("Apellido Paterno", self)
        self.apeP_l.setGeometry(480,100, 150, 20)
        self.apeP_t=QLineEdit(self)
        self.apeP_t.setGeometry(480, 120, 485, 20)

        self.telefono_l=QLabel("Numero de Telefono", self)
        self.telefono_l.setGeometry(60,140, 100, 20)
        self.telefono_t=QLineEdit(self)
        self.telefono_t.setGeometry(60,160, 750, 20)

        self.edad_l=QLabel('Edad', self)
        self.edad_l.setGeometry(817,140, 100, 20)
        self.edad_t=QLineEdit(self)
        self.edad_t.setGeometry(820,160, 145, 20)

        self.correo_l=QLabel('Correo Electronico', self)
        self.correo_l.setGeometry(60,180, 100, 20)
        self.correo_t=QLineEdit(self)
        self.correo_t.setGeometry(60,200, 905, 20)

        self.direccion_l=QLabel('Direccion', self)
        self.direccion_l.setGeometry(60,220, 100, 20)
        self.direccion_t=QLineEdit(self)
        self.direccion_t.setGeometry(60,240, 905, 20)

        self.puesto_l = QLabel("Puesto", self)
        self.puesto_l.setGeometry(60, 260, 100, 20)
        self.puesto_t = QLineEdit(self)
        self.puesto_t.setGeometry(60,280, 410, 20)

        self.carrera_l=QLabel("Carrera", self)
        self.carrera_l.setGeometry(480,260, 150, 20)
        self.carrera_t=QLineEdit(self)
        self.carrera_t.setGeometry(480, 280, 485, 20)

        self.gradoava_l = QLabel("Grado Avance", self)
        self.gradoava_l.setGeometry(60, 300, 100, 20)
        self.gradoava_t = QLineEdit(self)
        self.gradoava_t.setGeometry(60,320, 425, 20)

        self.estadociv_l=QLabel("Estado Civil", self)
        self.estadociv_l.setGeometry(495,300, 150, 20)
        self.estadociv_t=QLineEdit(self)
        self.estadociv_t.setGeometry(495, 320, 468, 20)

        self.escolaridad_l = QLabel("Escolaridad", self)
        self.escolaridad_l.setGeometry(60, 340, 100, 20)
        self.escolaridad_t = QLineEdit(self)
        self.escolaridad_t.setGeometry(60,360, 400, 20)

        self.sexo_l=QLabel("Sexo", self)
        self.sexo_l.setGeometry(470,340, 150, 20)
        self.sexo_t=QLineEdit(self)
        self.sexo_t.setGeometry(470, 360, 493, 20)

        self.habili_l=QLabel('Habilidades', self)
        self.habili_l.setGeometry(60,380, 100, 20)
        self.habili_t=QLineEdit(self)
        self.habili_t.setGeometry(60,400, 905, 20)

        self.botona_pag=QPushButton("Continuar", self)
        self.botona_pag.setGeometry(400, 450, 70, 30)

        self.botoncancelar=QPushButton("Cancelar", self)
        self.botoncancelar.setGeometry(60, 450, 70, 30)

    def limpiar(self):
        for child_widget in self.findChildren(QLineEdit):
            child_widget.clear()

class ventanaDetalles(QWidget):
    def __init__(self):
        super(ventanaDetalles, self).__init__()
        
        self.id_l = QLabel("Id", self)
        self.id_l.setGeometry(60,60, 120, 20)
        self.id_t = QLineEdit(self)
        self.id_t.setGeometry(60,80, 95, 20)
        self.id_t.setReadOnly(True)
        
        self.nom_l = QLabel("Nombre", self)
        self.nom_l.setGeometry(165,60, 120, 20)
        self.nom_t = QLineEdit(self)
        self.nom_t.setGeometry(165,80, 800, 20)
        self.nom_t.setReadOnly(True)
        
        self.apeM_l = QLabel("Apellido Materno", self)
        self.apeM_l.setGeometry(60, 100, 100, 20)
        self.apeM_t = QLineEdit(self)
        self.apeM_t.setGeometry(60,120, 410, 20)
        self.apeM_t.setReadOnly(True)
        
        self.apeP_l=QLabel("Apellido Paterno", self)
        self.apeP_l.setGeometry(480,100, 150, 20)
        self.apeP_t=QLineEdit(self)
        self.apeP_t.setGeometry(480, 120, 485, 20)
        self.apeP_t.setReadOnly(True)
        
        self.telefono_l=QLabel("Numero de Telefono", self)
        self.telefono_l.setGeometry(60,140, 100, 20)
        self.telefono_t=QLineEdit(self)
        self.telefono_t.setGeometry(60,160, 750, 20)
        self.telefono_t.setReadOnly(True)
        
        self.edad_l=QLabel('Edad', self)
        self.edad_l.setGeometry(817,140, 100, 20)
        self.edad_t=QLineEdit(self)
        self.edad_t.setGeometry(820,160, 145, 20)
        self.edad_t.setReadOnly(True)
        
        self.correo_l=QLabel('Correo Electronico', self)
        self.correo_l.setGeometry(60,180, 100, 20)
        self.correo_t=QLineEdit(self)
        self.correo_t.setGeometry(60,200, 905, 20)
        self.correo_t.setReadOnly(True)

        self.direccion_l=QLabel('Direccion', self)
        self.direccion_l.setGeometry(60,220, 100, 20)
        self.direccion_t=QLineEdit(self)
        self.direccion_t.setGeometry(60,240, 905, 20)
        self.direccion_t.setReadOnly(True)
        
        self.puesto_l = QLabel("Puesto", self)
        self.puesto_l.setGeometry(60, 260, 100, 20)
        self.puesto_t = QLineEdit(self)
        self.puesto_t.setGeometry(60,280, 410, 20)
        self.puesto_t.setReadOnly(True)

        self.carrera_l=QLabel("Carrera", self)
        self.carrera_l.setGeometry(480,260, 150, 20)
        self.carrera_t=QLineEdit(self)
        self.carrera_t.setGeometry(480, 280, 485, 20)
        self.carrera_t.setReadOnly(True)

        self.gradoava_l = QLabel("Grado Avance", self)
        self.gradoava_l.setGeometry(60, 300, 100, 20)
        self.gradoava_t = QLineEdit(self)
        self.gradoava_t.setGeometry(60,320, 425, 20)
        self.gradoava_t.setReadOnly(True)

        self.estadociv_l=QLabel("Estado Civil", self)
        self.estadociv_l.setGeometry(495,300, 150, 20)
        self.estadociv_t=QLineEdit(self)
        self.estadociv_t.setGeometry(495, 320, 468, 20)
        self.estadociv_t.setReadOnly(True)

        self.escolaridad_l = QLabel("Escolaridad", self)
        self.escolaridad_l.setGeometry(60, 340, 100, 20)
        self.escolaridad_t = QLineEdit(self)
        self.escolaridad_t.setGeometry(60,360, 400, 20)
        self.escolaridad_t.setReadOnly(True)

        self.sexo_l=QLabel("Sexo", self)
        self.sexo_l.setGeometry(470,340, 150, 20)
        self.sexo_t=QLineEdit(self)
        self.sexo_t.setGeometry(470, 360, 493, 20)
        self.sexo_t.setReadOnly(True)

        self.habili_l=QLabel('Habilidades', self)
        self.habili_l.setGeometry(60,380, 100, 20)
        self.habili_t=QLineEdit(self)
        self.habili_t.setGeometry(60,400, 905, 20)
        self.habili_t.setReadOnly(True)

        self.botona_pag=QPushButton("Continuar", self)
        self.botona_pag.setGeometry(400, 450, 70, 30)

        self.botoncancelar=QPushButton("Cancelar", self)
        self.botoncancelar.setGeometry(60, 450, 70, 30)

class aplicacion(QMainWindow):
    def __init__(self):
        super(aplicacion, self).__init__()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.apilar=QStackedWidget(self)
        self.pag1=vpuesto()
        self.candidatollenar=agregacandidato1()
        self.detalles=ventanaDetalles()
        self.edit=ventanaedit()
        self.apilar.addWidget(self.pag1)
        self.apilar.addWidget(self.candidatollenar)
        self.apilar.addWidget(self.detalles)
        self.apilar.addWidget(self.edit)
        self.setCentralWidget(self.apilar)
        self.apilar.setCurrentWidget(self.pag1)
        self.inicializar()

    def inicializar(self):
        screen_geometry = QApplication.primaryScreen().availableGeometry()
        window_width = 1000
        window_height = 800
        window_x = (screen_geometry.width() - window_width) // 2
        window_y = (screen_geometry.height() - window_height) // 2
        self.setGeometry(window_x, window_y, window_width, window_height)
        self.close_button = QPushButton("X", self)
        self.close_button.clicked.connect(self.close)
        self.close_button.setGeometry(960, 0, 40, 40)

        self.minimize_button = QPushButton("-", self)
        self.minimize_button.clicked.connect(self.showMinimized)
        self.minimize_button.setGeometry(920, 0, 40, 40)
          # Crear un degradado de color para el fondo
        gradient = QLinearGradient(0, 0, self.width(), 0)
        gradient.setColorAt(0, QColor("#06141b"))  # Color más oscuro a la izquierda
        gradient.setColorAt(0.5, QColor("#11212d")) 
        gradient.setColorAt(1, QColor("#5e503f")) 
            # Color más claro a la derecha
        # Establecer el degradado como fondo de la ventana
        palette = self.palette()
        palette.setBrush(QPalette.ColorGroup.All, QPalette.ColorRole.Window, QBrush(gradient))
        self.setPalette(palette)
        self.conexiones()

    def conexiones(self):
        self.pag1.agregar.clicked.connect(self.pedir_contra)
        self.pag1.detalles.clicked.connect(self.candidato)
        self.pag1.editar.clicked.connect(self.contraynombre)
        self.candidatollenar.botona_pag.clicked.connect(self.verificatodolleno)
        self.candidatollenar.botoncancelar.clicked.connect(self.cancelar_puesto)
        self.detalles.botona_pag.clicked.connect(self.aventprinci)
        self.detalles.botoncancelar.clicked.connect(self.aventprinci)
        self.edit.botoncancelar.clicked.connect(self.aventprinci)
        self.edit.botona_pag.clicked.connect(self.verificatodolleno2)

    def contraynombre(self):
            filas = self.obtener_filas()
            if filas > 0:
                ventanaEDI=ventanaemeeditar(self.correctos)
                ventanaEDI.exec()
            else:
                stilo = """QDialog {background-color: #072d44}"""
                self.setStyleSheet(stilo)
                QMessageBox.warning(self, "WARNING", "No hay nada para editar")

    def obtener_filas(self):
        return self.pag1.obtener_filas()

    def correctos(self):
        self.apilar.setCurrentWidget(self.edit)
        
    def aventprinci(self):
        self.apilar.setCurrentWidget(self.pag1)

    def candidato(self):
        ventanadet=ventanaemedetalles(self.existe)
        ventanadet.exec()

    def existe(self):
        self.apilar.setCurrentWidget(self.detalles)

    def cancelar_puesto(self):
        self.pag1.borrar_cancelar()
        self.candidatollenar.limpiar()
        self.apilar.setCurrentWidget(self.pag1)

    def verificatodolleno2(self):
        variables_a_verificar = [
            self.edit.id_t.text(),
            self.edit.nom_t.text(),
            self.edit.apeM_t.text(),
            self.edit.apeP_t.text(),
            self.edit.telefono_t.text(),
            self.edit.edad_t.text(),
            self.edit.correo_t.text(),
            self.edit.direccion_t.text(),
            self.edit.puesto_t.text(),
            self.edit.carrera_t.text(),
            self.edit.gradoava_t.text(),
            self.edit.estadociv_t.text(),
            self.edit.escolaridad_t.text(),
            self.edit.sexo_t.text(),
            self.edit.habili_t.text()
        ]
        if any(not campo.strip() for campo in variables_a_verificar):
            stilo = """QDialog {background-color: #072d44}"""
            self.setStyleSheet(stilo)
            QMessageBox.warning(self, "", "Todos los campos deben ser completados.")
        else:
            self.aventprinci()

    def verificatodolleno(self):
        variables_a_verificar = [
            self.candidatollenar.id_t.text(),
            self.candidatollenar.nom_t.text(),
            self.candidatollenar.apeM_t.text(),
            self.candidatollenar.apeP_t.text(),
            self.candidatollenar.telefono_t.text(),
            self.candidatollenar.edad_t.text(),
            self.candidatollenar.correo_t.text(),
            self.candidatollenar.direccion_t.text(),
            self.candidatollenar.puesto_t.text(),
            self.candidatollenar.carrera_t.text(),
            self.candidatollenar.gradoava_t.text(),
            self.candidatollenar.estadociv_t.text(),
            self.candidatollenar.escolaridad_t.text(),
            self.candidatollenar.sexo_t.text(),
            self.candidatollenar.habili_t.text()
        ]
        if any(not campo.strip() for campo in variables_a_verificar):
            stilo = """QDialog {background-color: #072d44}"""
            self.setStyleSheet(stilo)
            QMessageBox.warning(self, "", "Todos los campos deben ser completados.")
        else:
            self.ventanaprincipal()

    def ventanaprincipal(self):
        nombre_puesto=self.candidatollenar.nom_t.text()
        self.pag1.agregar_fila(nombre_puesto)
        self.pasoa_bd()
        self.edit.limpiar()
        self.candidatollenar.limpiar()
        self.apilar.setCurrentWidget(self.pag1)

    def pedir_contra(self):
        ventanac = ventanacontra(self.contracorrecta)
        ventanac.exec()

    def contracorrecta(self):
        self.apilar.setCurrentWidget(self.candidatollenar)

    def pasoa_bd(self):
        pass

    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
        self.dragPos = event.globalPosition().toPoint()
        event.accept()

class ventanaemeeditar(QDialog):
    def __init__(self, callback):
        super().__init__()
        self.callback2= callback
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        #self.tableWidget.setStyleSheet(style)
        self.close_button = QPushButton("X", self)
        self.close_button.clicked.connect(self.close)
        self.close_button.setGeometry(220, 0, 30, 30)
        self.setFixedSize(250, 230) 
        self.nombreP=QLabel('Ingrese el nombre del puesto:',self)
        self.nombreP.setGeometry(10,25,160,15)
        self.nombre=QLineEdit(self)
        self.contral = QLabel('Ingrese la contraseña:', self)
        self.contral.setGeometry(10,85,160,15)
        self.contra = QLineEdit(self)  
        verifica = QPushButton('Verificar', self)
        estilo = """QDialog {background-color: #072d44}"""
        self.setStyleSheet(estilo)
        verifica.clicked.connect(self.verificacontraynombre)
        layout = QVBoxLayout()
        layout.addWidget(self.nombre)
        layout.addWidget(self.contra)
        layout.addWidget(verifica)
        self.setLayout(layout)

    def verificacontraynombre(self):
        if self.contra.text()=='Secret' and self.nombre.text()=='1':
            print('si pasa')
            self.close()
            self.callback2()
        else:
            stilo = """QDialog {background-color: #072d44}"""
            self.setStyleSheet(stilo)
            QMessageBox.warning(self, 'Contraseña o id invalidos','Inténtelo de nuevo.')

class ventanaemedetalles(QDialog):
    def __init__(self, callback):
        super().__init__()
        self.callback3 = callback
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.close_button = QPushButton("X", self)
        self.close_button.clicked.connect(self.close)
        self.close_button.setGeometry(220, 0, 30, 30)
        self.setFixedSize(250, 150) 
        self.etiqueta = QLabel('Ingrese el nombre del Candidato', self)
        self.etiqueta.setGeometry(20, 10, 170, 30)
        self.id = QLineEdit(self)  
        self.verificaexis = QPushButton('Siguiente', self)
        estilo = """QDialog {background-color: #072d44}"""
        self.setStyleSheet(estilo)
        self.verificaexis.clicked.connect(self.verificaexistencia)
        layout = QVBoxLayout()
        layout.addWidget(self.id)
        layout.addWidget(self.verificaexis)
        self.setLayout(layout)

    def verificaexistencia(self):
        if self.id.text()=='1':
            print('si pasa')
            self.close()
            self.callback3()
        else:
            stilo = """QDialog {background-color: #072d44}"""
            self.setStyleSheet(stilo)
            QMessageBox.warning(self, '', 'No se encontro al candidato')

class ventanacontra(QDialog):
    def __init__(self, callback):
        super().__init__()
        self.callback = callback
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.close_button = QPushButton("X", self)
        self.close_button.clicked.connect(self.close)
        self.close_button.setGeometry(220, 0, 30, 30)
        self.setFixedSize(250, 150) 
        self.etiqueta = QLabel('Ingrese la contraseña:', self)
        self.etiqueta.setGeometry(20, 10, 170, 30)
        self.contra = QLineEdit(self)  
        self.verifica = QPushButton('Verificar', self)
        estilo = """QDialog {background-color: #072d44}"""
        self.setStyleSheet(estilo)
        self.verifica.clicked.connect(self.verificacontra)
        layout = QVBoxLayout()
        layout.addWidget(self.contra)
        layout.addWidget(self.verifica)
        self.setLayout(layout)

    def verificacontra(self):
        if self.contra.text()=='eladmin':
            print('si pasa')
            self.close()
            self.callback()
        else:
            stilo = """QDialog {background-color: #072d44}"""
            self.setStyleSheet(stilo)
            QMessageBox.warning(self, 'Contraseña incorrecta', 'La contraseña es incorrecta. Inténtelo de nuevo.')

if __name__ == '__main__':
    with open('styles.css', 'r') as f:
        style = f.read()
    app = QApplication(sys.argv)##administrar todo lo que se haga en la venta
    app.setStyleSheet(style)  # Aplicar el estilo global
    ventana = aplicacion()
    ventana.show()
    sys.exit(app.exec())
