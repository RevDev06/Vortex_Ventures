import sys
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *

class VPuesto(QWidget):
    def __init__(self):
        super(VPuesto, self).__init__()
        self.fila = 0
        self.columna = 2
        self.generartabla()

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

        self.agregar = QPushButton('Agregar Puesto')
        self.agregar.setFixedSize(100, 30)

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
        #self.agregar.clicked.connect(self.agregar_fila)
    

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

class Pag2(QWidget):
    def __init__(self):
        super(Pag2, self).__init__()

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
        self.remuneracion_t=QLineEdit(self)
        self.remuneracion_t.setText('')
        self.remuneracion_t.setGeometry(530, 200, 330, 20)

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

##botones 
        self.botona_pag = QPushButton("Continuar", self)
        self.botona_pag.setGeometry(400, 450, 70, 30)

        self.botoncancelar=QPushButton('Cancelar',self)
        self.botoncancelar.setGeometry(110, 450, 70, 30)

    def limpiar(self):
        for child_widget in self.findChildren(QLineEdit):
            child_widget.clear()

class Pag3(QWidget):
    def __init__(self):
        super(Pag3, self).__init__()

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

        self.condiciones_l=QLabel("Condiciones de Trabajo", self)
        self.condiciones_l.setGeometry(60,300, 300, 20)
        self.condiciones_t=QLineEdit(self)
        self.condiciones_t.setText('')
        self.condiciones_t.setGeometry(60, 320, 800, 20)

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
        self.botona_pag=QPushButton("Finalizar y Regresar", self)
        self.botona_pag.setGeometry(400, 400, 120, 30)

        self.botonregreso=QPushButton('Regresar', self)
        self.botonregreso.setGeometry(110, 400,120, 30)

    def limpiar(self):
        for child_widget in self.findChildren(QLineEdit):
            child_widget.clear()

class ventanaDetalles(QWidget):
    def __init__(self):
        super(ventanaDetalles, self).__init__()
        
        self.nom_l = QLabel("Nombre del Puesto", self)
        self.nom_l.setGeometry(60,60, 120, 20)
        self.nom_t = QLineEdit(self)
        self.nom_t.setText('')
        self.nom_t.setGeometry(60,80, 800, 20)
        self.nom_t.setReadOnly(True)
        
        self.codp_l = QLabel("Codigo de Puesto", self)
        self.codp_l.setGeometry(60, 100, 100, 20)
        self.codp_t = QLineEdit(self)
        self.codp_t.setText('')
        self.codp_t.setGeometry(60,120, 400, 20)
        self.codp_t.setReadOnly(True)
        
        self.area_l=QLabel("Area de adscripcion", self)
        self.area_l.setGeometry(475,100, 150, 20)
        self.area_t=QLineEdit(self)
        self.area_t.setText('')
        self.area_t.setGeometry(475, 120, 385, 20)
        self.area_t.setReadOnly(True)
        
        self.super_l=QLabel("Puesto del Jefe Superiro", self)
        self.super_l.setGeometry(60,140, 100, 20)
        self.super_t=QLineEdit(self)
        self.super_t.setText('')
        self.super_t.setGeometry(60,160, 800, 20)
        self.super_t.setReadOnly(True)
        
        self.jornada_l=QLabel("Jornada", self)
        self.jornada_l.setGeometry(60,180, 100, 20)
        self.jornada_t=QLineEdit(self)
        self.jornada_t.setText('')
        self.jornada_t.setGeometry(60,200, 450, 20)
        self.jornada_t.setReadOnly(True)
        
        self.remuneracion_l=QLabel("Remuneracion Mensual", self)
        self.remuneracion_l.setGeometry(530, 180, 200, 20)
        self.remuneracion_t=QLineEdit(self)
        self.remuneracion_t.setText('')
        self.remuneracion_t.setGeometry(530, 200, 330, 20)
        self.remuneracion_t.setReadOnly(True)
        
        self.prestaciones_l=QLabel("Presentaciones",self)
        self.prestaciones_l.setGeometry(60, 220, 800, 20)
        self.prestaciones_t=QLineEdit(self)
        self.prestaciones_t.setText('')
        self.prestaciones_t.setGeometry(60, 240, 800, 20)
        self.prestaciones_t.setReadOnly(True)

        self.descripccion_l=QLabel("Descripcion General",self)
        self.descripccion_l.setGeometry(60,260, 150, 20)
        self.descripccion_t=QLineEdit(self)
        self.descripccion_t.setText('')
        self.descripccion_t.setGeometry(60,280, 800, 20)
        self.descripccion_t.setReadOnly(True)
        
        self.funciones_l=QLabel("Funciones", self)
        self.funciones_l.setGeometry(60, 300, 100, 20)
        self.funciones_t=QLineEdit(self)
        self.funciones_t.setText('')
        self.funciones_t.setGeometry(60, 320, 800, 20)
        self.funciones_t.setReadOnly(True)

        self.edad_l=QLabel("Edad", self)
        self.edad_l.setGeometry(60, 340, 100, 20)
        self.edad_t=QLineEdit(self)
        self.edad_t.setText('')
        self.edad_t.setGeometry(60,360, 250, 20)
        self.edad_t.setReadOnly(True)

        self.sexo_l=QLabel("Sexo",self)
        self.sexo_l.setGeometry(340,340, 100, 20)
        self.sexo_t=QLineEdit(self)
        self.sexo_t.setText('')
        self.sexo_t.setGeometry(340,360, 250, 20)
        self.sexo_t.setReadOnly(True)
        
        self.civil_l=QLabel("Estado Civi", self)
        self.civil_l.setGeometry(610,340, 150, 20)
        self.civil_t=QLineEdit(self)
        self.civil_t.setText('')
        self.civil_t.setGeometry(610,360, 250, 20)
        self.civil_t.setReadOnly(True)

        self.escolaridad_l=QLabel("Escolaridad", self)
        self.escolaridad_l.setGeometry(60,380, 150, 20)
        self.escolaridad_t=QLineEdit(self)
        self.escolaridad_t.setText('')
        self.escolaridad_t.setGeometry(60,400, 250, 20)
        self.escolaridad_t.setReadOnly(True)

        self.gradoa_l=QLabel("Grado Avance", self)
        self.gradoa_l.setGeometry(340,380, 150, 20)
        self.gradoa_t=QLineEdit(self)
        self.gradoa_t.setText('')
        self.gradoa_t.setGeometry(340,400, 250, 20)
        self.gradoa_t.setReadOnly(True)

        self.carrera_l=QLabel("Carrera", self)
        self.carrera_l.setGeometry(610,380, 100, 20)
        self.carrera_t=QLineEdit(self)
        self.carrera_t.setText('')
        self.carrera_t.setGeometry(610,400, 250, 20)
        self.carrera_t.setReadOnly(True)


##boton
        self.botona_pag = QPushButton("Continuar", self)
        self.botona_pag.setGeometry(400, 450, 70, 30)

        self.botoncancelar=QPushButton("Salir", self)
        self.botoncancelar.setGeometry(110, 450, 70, 30)

class ventanadetalles2(QWidget):
    def __init__(self):
        super(ventanadetalles2, self).__init__()
        
        self.experiencia_l=QLabel("Experiencia", self)
        self.experiencia_l.setGeometry(60,60, 100, 20)
        self.experiencia_t=QLineEdit(self)
        self.experiencia_t.setText('')
        self.experiencia_t.setGeometry(60,80, 800, 20)
        self.experiencia_t.setReadOnly(True)

        self.conocimentos_l=QLabel("Conocimientos", self)
        self.conocimentos_l.setGeometry(60,100, 150, 20)
        self.conocimentos_t=QLineEdit(self)
        self.conocimentos_t.setText('')
        self.conocimentos_t.setGeometry(60,120, 800, 20)
        self.conocimentos_t.setReadOnly(True)

        self.mequipo_l=QLabel("Manejo de Equipo",self)
        self.mequipo_l.setGeometry(60,140, 200, 20)
        self.mequipo_t=QLineEdit(self)
        self.mequipo_t.setText('')
        self.mequipo_t.setGeometry(60,160, 800, 20)
        self.mequipo_t.setReadOnly(True)

        self.rfisicos_l=QLabel("Requisitos Fisicos", self)
        self.rfisicos_l.setGeometry(60,180, 200, 20)
        self.rfisicos_t=QLineEdit(self)
        self.rfisicos_t.setText('')
        self.rfisicos_t.setGeometry(60, 200, 800, 20)
        self.rfisicos_t.setReadOnly(True)

        self.rpsicologicos_l=QLabel("Requisitos Psicologicos", self)
        self.rpsicologicos_l.setGeometry(60, 220, 250, 20)
        self.rpsicologicos_t=QLineEdit(self)
        self.rpsicologicos_t.setText('')
        self.rpsicologicos_t.setGeometry(60, 240, 800, 20)
        self.rpsicologicos_t.setReadOnly(True)

        self.responsabilidades_l=QLabel("Responsabilidades", self)
        self.responsabilidades_l.setGeometry(60 ,260, 200, 20)
        self.responsabilidades_t=QLineEdit(self)
        self.responsabilidades_t.setText('')
        self.responsabilidades_t.setGeometry(60,280, 800, 20)
        self.responsabilidades_t.setReadOnly(True)

        self.condiciones_l=QLabel("Condiciones de Trabajo", self)
        self.condiciones_l.setGeometry(60,300, 300, 20)
        self.condiciones_t=QLineEdit(self)
        self.condiciones_t.setText('')
        self.condiciones_t.setGeometry(60, 320, 800, 20)
        self.condiciones_t.setReadOnly(True)

        self.idiomas_l=QLabel("Idiomas", self)
        self.idiomas_l.setGeometry(60,340, 100, 20)
        self.idiomast_t=QLineEdit(self)
        self.idiomast_t.setText('')
        self.idiomast_t.setGeometry(60,360, 385, 20)
        self.idiomast_t.setReadOnly(True)

        self.habilidades_l=QLabel("Habilidades", self)
        self.habilidades_l.setGeometry(475, 340, 150, 20)
        self.habilidades_t=QLineEdit(self)
        self.habilidades_t.setText('')
        self.habilidades_t.setGeometry(475,360, 385, 20)
        self.habilidades_t.setReadOnly(True)

#Boton
        self.botona_pag=QPushButton("Salir", self)
        self.botona_pag.setGeometry(400, 400, 120, 30)
        
        self.botoncancelar=QPushButton("Regresar", self)
        self.botoncancelar.setGeometry(60, 400, 70, 30)

class ventanaeditar(QWidget):
    def __init__(self):
        super(ventanaeditar, self).__init__()
        
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
        self.remuneracion_t=QLineEdit(self)
        self.remuneracion_t.setText('')
        self.remuneracion_t.setGeometry(530, 200, 330, 20)

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

#boton
        self.botona_pag=QPushButton("Continuar", self)
        self.botona_pag.setGeometry(400, 450, 70, 30)

        self.botoncancelar=QPushButton("Cancelar", self)
        self.botoncancelar.setGeometry(60, 450, 70, 30)

class ventanaeditar2(QWidget):
    def __init__(self):
        super(ventanaeditar2, self).__init__()
        
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

        self.condiciones_l=QLabel("Condiciones de Trabajo", self)
        self.condiciones_l.setGeometry(60,300, 300, 20)
        self.condiciones_t=QLineEdit(self)
        self.condiciones_t.setText('')
        self.condiciones_t.setGeometry(60, 320, 800, 20)

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

        self.botona_pag=QPushButton("Guardar y Regresar",self)
        self.botona_pag.setGeometry(400, 400, 120, 30)

        self.botoncancelar=QPushButton("Regresar", self)
        self.botoncancelar.setGeometry(60, 400, 70, 30)

class aplicacion(QMainWindow):
    def __init__(self):
        super(aplicacion, self).__init__()

        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        self.apilar=QStackedWidget(self)
        self.pag1=VPuesto()
        self.pag2=Pag2()
        self.pag3=Pag3()
        self.ventanad=ventanaDetalles()
        self.ventanad2=ventanadetalles2()
        self.ventanaedit=ventanaeditar()
        self.ventanaedit2=ventanaeditar2()
        self.apilar.addWidget(self.pag1)
        self.apilar.addWidget(self.pag2)
        self.apilar.addWidget(self.pag3)
        self.apilar.addWidget(self.ventanad)
        self.apilar.addWidget(self.ventanad2)
        self.apilar.addWidget(self.ventanaedit)
        self.apilar.addWidget(self.ventanaedit2)
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

        self.setWindowTitle('Ventanas Puesto')
        self.conexiones()

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

    def conexiones(self):
        self.pag1.agregar.clicked.connect(self.pedir_contra)
        self.pag2.botona_pag.clicked.connect(self.verificatodolleno)
        self.pag3.botona_pag.clicked.connect(self.verificatodolleno2)
        self.pag3.botonregreso.clicked.connect(self.cambioa_pag2)
        self.pag2.botoncancelar.clicked.connect(self.cancelar_puesto)
        self.pag1.detalles.clicked.connect(self.id_puesto)
        self.ventanad.botoncancelar.clicked.connect(self.cambioa_pag11)
        self.ventanad.botona_pag.clicked.connect(self.ventanaDet2)
        self.ventanad2.botoncancelar.clicked.connect(self.ventanaDet)
        self.ventanad2.botona_pag.clicked.connect(self.cambioa_pag11)
        self.pag1.editar.clicked.connect(self.contraynombreP)
        self.ventanaedit.botoncancelar.clicked.connect(self.cambioa_pag11)
        self.ventanaedit.botona_pag.clicked.connect(self.verifica)
        self.ventanaedit2.botona_pag.clicked.connect(self.verifica2)
        self.ventanaedit2.botoncancelar.clicked.connect(self.aventanaedi)

    def verifica(self):
        variables_a_verificar = [
            self.ventanaedit.nom_t.text(),
            self.ventanaedit.codp_t.text(),
            self.ventanaedit.area_t.text(),
            self.ventanaedit.super_t.text(),
            self.ventanaedit.jornada_t.text(),
            self.ventanaedit.remuneracion_t.text(),
            self.ventanaedit.prestaciones_t.text(),
            self.ventanaedit.descripccion_t.text(),
            self.ventanaedit.funciones_t.text(),
            self.ventanaedit.edad_t.text(),
            self.ventanaedit.sexo_t.text(),
            self.ventanaedit.civil_t.text(),
            self.ventanaedit.escolaridad_t.text(),
            self.ventanaedit.gradoa_t.text(),
            self.ventanaedit.carrera_t.text()
              ]
        if any(not campo.replace(" ", "") for campo in variables_a_verificar):
            stilo = """QDialog {background-color: #072d44}"""
            self.setStyleSheet(stilo)
            QMessageBox.warning(self, "Campos Vacíos", "Todos los campos deben ser completados.")
        else:
            self.ventanaedi2()
        
    def verifica2(self):
        variables_a_verificar = [
            self.ventanaedit2.experiencia_t.text(),
            self.ventanaedit2.conocimentos_t.text(),
            self.ventanaedit2.mequipo_t.text(),
            self.ventanaedit2.rfisicos_t.text(),
            self.ventanaedit2.rpsicologicos_t.text(),
            self.ventanaedit2.responsabilidades_t.text(),
            self.ventanaedit2.condiciones_t.text(),
            self.ventanaedit2.idiomast_t.text(),
            self.ventanaedit2.habilidades_t.text()
        ]
        if any(not campo.strip() for campo in variables_a_verificar):
            stilo = """QDialog {background-color: #072d44}"""
            self.setStyleSheet(stilo)
            QMessageBox.warning(self, "Campos Vacíos", "Todos los campos deben ser completados.")
        else:
            self.cambioa_pag111()    

    def verificatodolleno(self):
        variables_a_verificar = [
            self.pag2.nom_t.text(),
            self.pag2.codp_t.text(),
            self.pag2.area_t.text(),
            self.pag2.super_t.text(),
            self.pag2.jornada_t.text(),
            self.pag2.remuneracion_t.text(),
            self.pag2.prestaciones_t.text(),
            self.pag2.descripccion_t.text(),
            self.pag2.funciones_t.text(),
            self.pag2.edad_t.text(),
            self.pag2.sexo_t.text(),
            self.pag2.civil_t.text(),
            self.pag2.escolaridad_t.text(),
            self.pag2.gradoa_t.text(),
            self.pag2.carrera_t.text()]
        if any(not campo.strip() for campo in variables_a_verificar):
            stilo = """QDialog {background-color: #072d44}"""
            self.setStyleSheet(stilo)
            QMessageBox.warning(self, "Campos Vacíos", "Todos los campos deben ser completados.")
            
        else:
            self.cambioa_pag3()

    def verificatodolleno2(self):
        variables_a_verificar = [
            self.pag3.experiencia_t.text(),
            self.pag3.conocimentos_t.text(),
            self.pag3.mequipo_t.text(),
            self.pag3.rfisicos_t.text(),
            self.pag3.rpsicologicos_t.text(),
            self.pag3.responsabilidades_t.text(),
            self.pag3.condiciones_t.text(),
            self.pag3.idiomast_t.text(),
            self.pag3.habilidades_t.text()
        ]
        if any(not campo.strip() for campo in variables_a_verificar):
            stilo = """QDialog {background-color: #072d44}"""
            self.setStyleSheet(stilo)
            QMessageBox.warning(self, "Campos Vacíos", "Todos los campos deben ser completados.")
        else:
            self.cambioa_pag1()




    def obtener_filas(self):
        return self.pag1.obtener_filas()



    def contraynombreP(self):
        filas = self.obtener_filas()
        if filas > 0:
            ventanaEDI=ventanaemeeditar(self.contraynombrecorrectos)
            ventanaEDI.exec()
        else:
            stilo = """QDialog {background-color: #072d44}"""
            self.setStyleSheet(stilo)
            QMessageBox.warning(self, "", "No hay nada para editar")

    def cambioa_pag111(self):
        self.variables_pag3()
        self.pasoa_bd()
        self.apilar.setCurrentWidget(self.pag1)

    def ventanaedi2(self):
        self.variables_pag2()
        self.apilar.setCurrentWidget(self.ventanaedit2)

    def aventanaedi(self):
        self.apilar.setCurrentWidget(self.ventanaedit)

    def ventanaDet2(self):
        self.apilar.setCurrentWidget(self.ventanad2)

    def ventanaDet(self):
        self.apilar.setCurrentWidget(self.ventanad)

    def cancelar_puesto(self):
        self.pag1.borrar_cancelar()
        self.apilar.setCurrentWidget(self.pag1)

    def cambioa_pag11(self):
        self.apilar.setCurrentWidget(self.pag1)

    def cambioa_pag2(self):
        self.apilar.setCurrentWidget(self.pag2)
    
    def cambioa_pag3(self):
        self.apilar.setCurrentWidget(self.pag3)
        self.variables_pag2()

    def cambioa_pag1(self):
        nombre_puesto=self.pag2.nom_t.text()
        self.pag1.agregar_fila(nombre_puesto)
        self.apilar.setCurrentWidget(self.pag1)
        self.variables_pag3()
        self.pasoa_bd()
        self.pag2.limpiar()
        self.pag3.limpiar()    

    def id_puesto(self):
        ventanadet=ventanaemedetalles(self.id_correcto)
        ventanadet.exec()

    def id_correcto(self):
        self.apilar.setCurrentWidget(self.ventanad)

    def contraynombreP(self):
        ventanaEDI=ventanaemeeditar(self.contraynombrecorrectos)
        ventanaEDI.exec()

    def contraynombrecorrectos(self):
        self.apilar.setCurrentWidget(self.ventanaedit)

    def pedir_contra(self):
        ventanac = ventanacontra(self.contracorrecta)
        ventanac.exec()

    def contracorrecta(self):
        self.apilar.setCurrentWidget(self.pag2)

    def variables_pag2(self):
        self.nombre=self.pag2.nom_t.text()
        self.codigo_puesto=self.pag2.codp_t.text()
        self.area_adscripcion=self.pag2.area_t.text()
        self.puesto_jefe=self.pag2.super_t.text()
        self.Jornada=self.pag2.jornada_t.text()
        self.remuneracion=self.pag2.remuneracion_t.text()
        self.prestaciones=self.pag2.prestaciones_t.text()
        self.descripccion_general=self.pag2.descripccion_t.text()
        self.funcion=self.pag2.funciones_t.text()
        self.edad=self.pag2.edad_t.text()
        self.sexo=self.pag2.sexo_t.text()
        self.estado_civil=self.pag2.civil_t.text()
        self.escolaridad=self.pag2.escolaridad_t.text()
        self.grado_avance=self.pag2.gradoa_t.text()
        self.carrera=self.pag2.carrera_t.text()

    def variables_pag3(self):
        self.experienci=self.pag3.experiencia_t.text()
        self.conocimientos=self.pag3.conocimentos_t.text()
        self.manejo_equipo=self.pag3.mequipo_t.text()
        self.requisitosF=self.pag3.rfisicos_t.text()
        self.requisitosP=self.pag3.rpsicologicos_t.text()
        self.responsabilidades=self.pag3.responsabilidades_t.text()
        self.condiciones=self.pag3.condiciones_t.text()
        self.idiomas=self.pag3.idiomast_t.text()
        self.habilidades=self.pag3.habilidades_t.text()

    def pasoa_bd(self):
        pass

    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
        self.dragPos = event.globalPosition().toPoint()
        event.accept()

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
        if self.contra.text()=='Secret':
            print('si pasa')
            self.close()
            self.callback()
        else:
            stilo = """QDialog {background-color: #072d44}"""
            self.setStyleSheet(stilo)
            QMessageBox.warning(self, 'Contraseña incorrecta', 'La contraseña es incorrecta. Inténtelo de nuevo.')

class ventanaemedetalles(QDialog):
    def __init__(self, callback):
        super().__init__()
        self.callback3 = callback
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.close_button = QPushButton("X", self)
        self.close_button.clicked.connect(self.close)
        self.close_button.setGeometry(220, 0, 30, 30)
        self.setFixedSize(250, 150) 
        self.etiqueta = QLabel('Ingrese el nombre del Puesto', self)
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
            QMessageBox.warning(self, 'Id no encontrada', 'La Id es incorrecta. Inténtelo de nuevo.')

class ventanaemeeditar(QDialog):
    def __init__(self, callback):
        super().__init__()
        self.callback2= callback
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.tableWidget.setStyleSheet(style)
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


if __name__ == '__main__':
    with open('styles.css', 'r') as f:
        style = f.read()
    app = QApplication(sys.argv)##administrar todo lo que se haga en la venta
    app.setStyleSheet(style)  # Aplicar el estilo global
    ventana = aplicacion()
    ventana.show()
    sys.exit(app.exec())
