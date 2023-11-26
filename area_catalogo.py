import sys
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *

class VArea(QWidget):
    def __init__(self):
        super(VArea, self).__init__()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.fila = 0
        self.columna = 3
        self.inicializar()
        self.generartabla()

    def inicializar(self):
        self.resize(1000, 800)

        # Crear un degradado de color para el fondo
        gradient = QLinearGradient(0, 0, self.width(), 0)
        gradient.setColorAt(0, QColor("#0e212c"))  # Color más claro a la izquierda
        gradient.setColorAt(0.5, QColor("#43423b"))  # Color más oscuro a la derecha
        gradient.setColorAt(1,QColor("#816d50"))
        # Establecer el degradado como fondo de la ventana
        palette = self.palette()
        palette.setBrush(QPalette.ColorGroup.All, QPalette.ColorRole.Window, QBrush(gradient))
        self.setPalette(palette)
        
        self.close_button = QPushButton("X", self)
        self.close_button.clicked.connect(self.close)
        self.close_button.setGeometry(960, 0, 40, 40)
        self.minimize_button = QPushButton("-", self)
        self.minimize_button.clicked.connect(self.showMinimized)
        self.minimize_button.setGeometry(920, 0, 40, 40)

    def generartabla(self):
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(self.fila)
        self.tableWidget.setColumnCount(self.columna)  

        column_width = 325
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        for i in range(self.columna):
            self.tableWidget.setColumnWidth(i, column_width)

        self.agregar = QPushButton('Agregar Area')
        self.agregar.setFixedSize(100, 30)
        self.agregar.clicked.connect(self.contra)

        self.editar = QPushButton('Editar')
        self.editar.setFixedSize(100, 30)
        self.editar.clicked.connect(self.editar_fila)

        blayout = QHBoxLayout()
        blayout.addWidget(self.agregar)
        blayout.addWidget(self.editar)
        layout = QVBoxLayout(self)
        layout.addLayout(blayout)
        layout.addWidget(self.tableWidget)

    def editar_fila(self):
        masuna = self.tableWidget.rowCount()
        if masuna > 0:
                self.contra2()
        else:
            QMessageBox.warning(self, "", "No hay nada para editar")

    def contra2(self):
        ventana= ventanacontra(self.nuevosdatos)
        ventana.exec()

    def contra(self):
        ventana= ventanacontra(self.pedir_nombre)
        ventana.exec()

    def nuevosdatos(self):
        ventanita = emergente2()
        result = ventanita.exec()
        if result == QDialog.DialogCode.Accepted:
            nombre = ventanita.nombre.text()
            id = ventanita.Id.text()
            id2=ventanita.Id2.text()
            self.buscar(id2,nombre,id)

    def buscar(self,idbuscar,nnombre,nid):
        for fila in range(self.tableWidget.rowCount()):
            idenfila = self.tableWidget.item(fila, 0).text()
            if idenfila == idbuscar:
                self.tableWidget.item(fila, 0).setText(nid)
                self.tableWidget.item(fila, 1).setText(nnombre)
            else:
                stilo = """QDialog {background-color: #072d44}"""
                self.setStyleSheet(stilo)
                QMessageBox.warning(self, "", "No esxiste ningun area con esa Id")

    def cambio(self):
        pass

    def pedir_nombre(self):
        ventanita = emergente()
        result = ventanita.exec()
        if result == QDialog.DialogCode.Accepted:
            nombre = ventanita.nombre.text()
            id = ventanita.Id.text()
            self.agregar_fila(nombre, id)

    def crearfila(self,nombre):
        nombre, id, accepted = self.pedir_nombre()
        if accepted:
            self.agregar_fila(nombre, id)
    
    def agregar_fila(self, nombre, id):
        self.fila += 1
        self.tableWidget.setRowCount(self.fila)

        ID= QTableWidgetItem(id)
        ID.setTextAlignment(0x0104 | 0x0180)  # Qt.AlignmentFlag.AlignCenter
        self.tableWidget.setItem(self.fila - 1, 0, ID)

        puesto = QTableWidgetItem(nombre)
        puesto.setTextAlignment(0x0104 | 0x0180)  # Qt.AlignmentFlag.AlignCenter          
        self.tableWidget.setItem(self.fila - 1, 1, puesto)

        borrar = QPushButton('Borrar')
        self.tableWidget.setCellWidget(self.fila - 1, 2, borrar)
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

class emergente(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.close_button = QPushButton("X", self)
        self.close_button.clicked.connect(self.reject)
        self.close_button.setGeometry(220, 0, 30, 30)
        self.setFixedSize(250, 230) 
        self.nombreP=QLabel('Ingrese el nombre:',self)
        self.nombreP.setGeometry(10,25,160,15)
        self.nombre=QLineEdit(self)
        self.Idl = QLabel('Ingrese el Id:', self)
        self.Idl.setGeometry(10,85,160,15)
        self.Id = QLineEdit(self)  
        verifica = QPushButton('Verificar', self)
        stilo = """QDialog {background-color: #072d44}"""
        self.setStyleSheet(stilo)
        verifica.clicked.connect(self.campos)
        layout = QVBoxLayout()
        layout.addWidget(self.nombre)
        layout.addWidget(self.Id)
        layout.addWidget(verifica)
        self.setLayout(layout)

    def campos(self):
        nombre_texto = self.nombre.text().strip()
        id_texto = self.Id.text().strip()

        if not nombre_texto or not id_texto:
            stilo = """QDialog {background-color: #072d44}"""
            self.setStyleSheet(stilo)
            QMessageBox.warning(self, "Campos Vacíos", "Ambos campos deben ser completados.")
        else:
            self.accept()

class emergente2(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.close_button = QPushButton("X", self)
        self.close_button.clicked.connect(self.reject)
        self.close_button.setGeometry(220, 0, 30, 30)
        self.setFixedSize(250, 230) 
        self.nombreP=QLabel('Ingrese el nuevo nombre:',self)
        self.nombreP.setGeometry(10,15,160,15)
        self.nombre=QLineEdit(self)
        self.Idl = QLabel('Ingrese el nuevo Id:', self)
        self.Idl.setGeometry(10,62,160,15)
        self.Id = QLineEdit(self)  
        self.Idl2=QLabel('Ingrese el id del area a cambiar:', self)
        self.Idl2.setGeometry(10,108,160,15)
        self.Id2 = QLineEdit(self)  
        verifica = QPushButton('Verificar', self)
        stilo = """QDialog {background-color: #072d44}"""
        self.setStyleSheet(stilo)
        verifica.clicked.connect(self.campos)
        layout = QVBoxLayout()
        layout.addWidget(self.nombre)
        layout.addWidget(self.Id)
        layout.addWidget(self.Id2)
        layout.addWidget(verifica)
        self.setLayout(layout)

    def campos(self):
        nombre_texto = self.nombre.text().strip()
        id_texto = self.Id.text().strip()
        if not nombre_texto or not id_texto:
            stilo = """QDialog {background-color: #072d44}"""
            self.setStyleSheet(stilo)
            QMessageBox.warning(self, "Campos Vacíos", "Los campos deben ser completados.")
        else:
            self.accept()

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
        stilo = """QDialog {background-color: #072d44}"""
        self.setStyleSheet(stilo)
        self.verifica.clicked.connect(self.verificacontra)
        layout = QVBoxLayout()
        layout.addWidget(self.contra)
        layout.addWidget(self.verifica)
        self.setLayout(layout)
    def verificacontra(self):
        if self.contra.text()=='Secret':
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
    ventana = VArea()
    ventana.show()
    sys.exit(app.exec())
