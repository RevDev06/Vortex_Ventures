import sys
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QStackedWidget, QMainWindow, QWidget, QTableWidget, QPushButton, QVBoxLayout, QLabel

class VPuesto(QWidget):
    def __init__(self):
        super().__init__()
        self.fila = 0
        self.columna = 4
        self.generartabla()

    def generartabla(self):
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(self.fila)
        self.tableWidget.setColumnCount(self.columna)  

        self.tableWidget.setStyleSheet("QTableWidget { background-color: black; }")
        self.tableWidget.setStyleSheet("QTableWidget::item { border: .2px solid black; }")
        column_width = 140
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        for i in range(self.columna):
            self.tableWidget.setColumnWidth(i, column_width)

        self.agregar = QPushButton('Agregar Puesto')
        self.agregar.setFont(QFont('Bond', 8))
        self.agregar.setFixedSize(90, 23)

        self.agregar.clicked.connect(self.agregar_fila)
        layout = QVBoxLayout(self)
        layout.addWidget(self.agregar)
        layout.addWidget(self.tableWidget)

    def agregar_fila(self):
        self.fila += 1
        self.tableWidget.setRowCount(self.fila)
        puesto = QLabel(f'Pulse editar {self.fila}')
        puesto.setAlignment(Qt.AlignmentFlag.AlignCenter)           
        self.tableWidget.setCellWidget(self.fila - 1, 0, puesto)

        detalles = QPushButton('Detalles')
        self.tableWidget.setCellWidget(self.fila - 1, 1, detalles)

        editar = QPushButton('Editar')
        self.tableWidget.setCellWidget(self.fila - 1, 2, editar)

        borrar = QPushButton('Borrar')
        self.tableWidget.setCellWidget(self.fila - 1, 3, borrar)
        borrar.clicked.connect(self.borra)

    def borra(self):
        index = self.tableWidget.indexAt(self.sender().pos())
        if index.isValid():
            fila = index.row()
            self.tableWidget.removeRow(fila)
            self.fila -= 1

class Ventana2(QWidget):
    def __init__(self):
        super(Ventana2, self).__init__()
        layout=QVBoxLayout
        self.boton = QPushButton('Regresar a la Pagina 1', self)
        self.boton.setFont(QFont('Bond',8))
        self.boton.move(100, 150)
        self.boton.setFixedSize(120, 25)

class Aplicacion(QMainWindow):
    def __init__(self):
        super(Aplicacion, self).__init__()
        self.apilacion_widget = QStackedWidget(self)
        self.pag1 = VPuesto()
        self.pag2 = Ventana2()
        self.apilacion_widget.addWidget(self.pag1)
        self.apilacion_widget.addWidget(self.pag2)
        self.setCentralWidget(self.apilacion_widget)
        self.apilacion_widget.setCurrentWidget(self.pag1)
        self.inicializar_ui()

    def inicializar_ui(self):
        self.resize(800, 800)
        self.setWindowTitle('Puesto')
        self.conexiones()

    def conexiones(self):
        self.pag1.agregar.clicked.connect(self.cambioa_pag2)
        self.pag2.boton.clicked.connect(self.cambioa_pag1)

    def cambioa_pag2(self):
        self.apilacion_widget.setCurrentWidget(self.pag2)

    def cambioa_pag1(self):
        self.apilacion_widget.setCurrentWidget(self.pag1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Aplicacion()
    ventana.show()
    sys.exit(app.exec())
