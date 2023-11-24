import sys
from PyQt6.QtWidgets import (QApplication, QWidget,QLabel,QLineEdit, QPushButton)
from PyQt6.QtGui import QFont 
from PyQt6.QtCore import QSize,Qt,QLocale
##crear una ventana
class v(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializarUI()

    def inicializarUI(self):
        #configurar ventana
      self.setGeometry(100,50,1000,800)
      self.setWindowTitle("Analisis")
      self.generar_analisis()
      self.show() ##visualice la ventana

    def generar_analisis(self):
##titulo
      titulo_label= QLabel(self)
      titulo_label.setText("Autorización De Requisición")
      titulo_label.setFont(QFont('Arial',18))
      titulo_label.move(350,15)
#folio
      folio_label= QLabel(self)
      folio_label.setText("<b>FOLIO</b>")
      folio_label.setFont(QFont('Arial',10))
      folio_label.move(20,70)

      self.folio_input= QLineEdit(self)
      self.folio_input.resize(250,24)
      self.folio_input.move(20,86)
#puesto vacante
      puesto_vacante_label = QLabel(self)
      puesto_vacante_label.setText("<b>Puesto Vacante</b>")
      puesto_vacante_label.setFont(QFont('Arial',10))
      puesto_vacante_label.move(301,70)

      self.puesto_vacante_input =QLineEdit(self)
      self.puesto_vacante_input.resize(380,24)
      self.puesto_vacante_input.move(301,86)
#números de vacantes
      n_vacantes_label = QLabel(self)
      n_vacantes_label.setText("<b>Número de Vacantes</b>")
      n_vacantes_label.setFont(QFont('Arial',10))
      n_vacantes_label.move(700,70)

      self.n_vacantes_input = QLineEdit(self)
      self.n_vacantes_input.resize(250,24)
      self.n_vacantes_input.move(700,86)
##revisado por:
      revisado_label = QLabel(self)
      revisado_label.setText("<b>Revisado por:</b>")
      revisado_label.setFont(QFont('Arial',10))
      revisado_label.move(20,120)

      self.revisado_input = QLineEdit(self)
      self.revisado_input.resize(930,24)
      self.revisado_input.move(20,140)
      
      nom_puesto = QLabel(self)
      nom_puesto.setText("Nombre y puesto")
      nom_puesto.setFont(QFont('Arial',10))
      nom_puesto.move(20,168)
##autorizado por:
      autorizado_label = QLabel(self)
      autorizado_label.setText("<b>Autorizado por:</b>")
      autorizado_label.setFont(QFont('Arial',10))
      autorizado_label.move(20,214)

      self.autorizado_input = QLineEdit(self)
      self.autorizado_input.resize(930,24)
      self.autorizado_input.move(20,234)
      
      nom_puesto2 = QLabel(self)
      nom_puesto2.setText("Nombre y puesto")
      nom_puesto2.setFont(QFont('Arial',10))
      nom_puesto2.move(20,262)
##button de enviar
      button =QPushButton(self)
      button.setText("Enviar Autorización")
      button.setFont(QFont('Arial',10))
      button.resize(120,35)
      button.move(20,304)

if __name__ == '__main__':
   with open('styles.css', 'r') as f:
        style = f.read()
   app = QApplication(sys.argv)##administrar todo lo que se haga en la venta
   app.setStyleSheet(style) 
   ventana = v()
   sys.exit(app.exec())#salir
