import sys
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidget, QPushButton, QVBoxLayout, QLabel, QStackedWidget


class Puesto(QWidget):
    def __init__(self):
        super(Puesto, self).__init__()
        self.fila = 0
        self.columna = 4
        self.generar()

    def generar(self):
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(self.fila)
        self.tableWidget.setColumnCount(self.columna)
        self.tableWidget.setGeometry(0, 30, 30, 50)

        self.tableWidget.setStyleSheet(
            "QTableWidget { background-color: black; }")
        self.tableWidget.setStyleSheet(
            "QTableWidget::item { border: .2px solid black; }")
        column_width = 144
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        for i in range(self.columna):
            self.tableWidget.setColumnWidth(i, column_width)

        agregar = QPushButton()
        agregar.setText('Agregar Puesto')
        agregar.clicked.connect(self.agregar_fila)

        layout = QVBoxLayout(self)
        layout.addWidget(agregar)
        layout.addWidget(self.tableWidget)

    def agregar_fila(self):
        self.fila += 1
        self.tableWidget.setRowCount(self.fila)

        puesto = QLabel('Pulse editar')
        puesto.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tableWidget.setCellWidget(self.fila - 1, 0, puesto)

        detalles = QPushButton('Detalles')
        self.tableWidget.setCellWidget(self.fila - 1, 1, detalles)

        self.editar = QPushButton('Editar')
        self.tableWidget.setCellWidget(self.fila - 1, 2, self.editar)
        # Connect the clicked signal here
        self.editar.clicked.connect(self.parent().cambio_a_editar)

        borrar = QPushButton('Borrar')
        self.tableWidget.setCellWidget(self.fila - 1, 3, borrar)
        borrar.clicked.connect(self.borra)

    def borra(self):
        index = self.tableWidget.indexAt(self.sender().pos())
        if index.isValid():
            fila = index.row()
            self.tableWidget.removeRow(fila)
            self.fila -= 1


class Puesto2(QWidget):
    def __init__(self):
        super(Puesto2, self).__init__()
        layout = QVBoxLayout(self)
        self.regreso = QPushButton('Regresar')
        layout.addWidget(self.regreso)


class Ventana(QMainWindow):
    def __init__(self):
        super(Ventana, self).__init__()
        self.ventana_widget = QStackedWidget(self)
        self.puesto = Puesto()
        self.puesto2 = Puesto2()
        self.ventana_widget.addWidget(self.puesto)
        self.ventana_widget.addWidget(self.puesto2)
        self.setCentralWidget(self.ventana_widget)
        self.ventana_widget.setCurrentWidget(self.puesto)
        self.inicializar_ui()

    def inicializar_ui(self):
        self.resize(600, 600)
        self.setWindowTitle("ey")
        self.conexion()

    def conexion(self):
        self.puesto2.regreso.clicked.connect(self.cambio_a_puesto)

    def cambio_a_editar(self):
        self.ventana_widget.setCurrentWidget(self.puesto2)

    def cambio_a_puesto(self):
        self.ventana_widget.setCurrentWidget(self.puesto)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
