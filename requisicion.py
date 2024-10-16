##ventana
import sys
from PyQt6.QtWidgets import (QApplication, QWidget,QLabel,QLineEdit, QPushButton,QDateTimeEdit,
QMessageBox, QCheckBox,QComboBox,QRadioButton)
from PyQt6.QtGui import QFont, QBrush, QLinearGradient, QPainter, QColor,QPalette
from PyQt6.QtCore import QSize,Qt,QLocale,QDateTime
from conex_db import database
##crear una ventana

con_db = database()
con_db.verifAndCreateDataBase()
con_db.select_db()

class vtn(QWidget):
       def __init__(self):
              super().__init__()
              self.inicializarUI()


       def inicializarUI(self):
              #configurar ventana
              self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
              screen_geometry = QApplication.primaryScreen().availableGeometry()
              window_width = 1000
              window_height = 800
              window_x = (screen_geometry.width() - window_width) // 2
              window_y = (screen_geometry.height() - window_height) // 2
              self.setGeometry(window_x, window_y, window_width, window_height)

              self.close_button = QPushButton("X", self)
              self.close_button.clicked.connect(self.close)
              self.close_button.setGeometry(960, 0, 40, 40)
              self.close_button.setStyleSheet("background-color:#5f5a4d; color:#ccc6ac;border-radius: 5px;")


              self.minimize_button = QPushButton("-", self)
              self.minimize_button.clicked.connect(self.showMinimized)
              self.minimize_button.setGeometry(920, 0, 40, 40)
              self.minimize_button.setStyleSheet("background-color:#867c61; color:#ccc6ac;border-radius: 5px;")

              self.generar_formulario()
              self.show() ##visualice la ventana

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
       
       def mousePressEvent(self, event):
            self.dragPos = event.globalPosition().toPoint()

       def mouseMoveEvent(self, event):
            self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
            self.dragPos = event.globalPosition().toPoint()
            event.accept()

       def generar_formulario(self):
              global fecha_elaboracion
              global reclutamiento
              global inicio_vacante
              global sender
              self.is_logged = False
       ##titulo
              titulo_label = QLabel(self)
              titulo_label.setText("Solicitud De Requisicion De Personal")
              titulo_label.setFont(QFont('Arial',16))
              titulo_label.move(350,15)
       ##folio
              folio_label = QLabel(self)
              folio_label.setText("FOLIO")
              folio_label.setFont(QFont('Arial',10))
              folio_label.move(20,54)
              ##campo para ingresar la informacion
              self.folio_input = QLineEdit(self)
              self.folio_input.resize(250,24)
              self.folio_input.move(20,74)
       ##area que solicita
              area_solicita_label = QLabel(self)
              area_solicita_label.setText("Area que solicita")
              area_solicita_label.setFont(QFont('Arial',10))
              area_solicita_label.move(310,54)
              ##QComboBox se utilizo para crear una barra desplegable para elegir una opcion
              ##addItems para poner las opciones
              self.area_solicita_input =QComboBox(self)
              self.area_solicita_input.addItems(["Elige","1","2","3"])
              self.area_solicita_input.currentText()
              self.area_solicita_input.resize(360,24)
              self.area_solicita_input.move(310,74)
       ##fecha de elaboracion
              fecha_elaboracion_label=QLabel(self)
              fecha_elaboracion_label.setText("Fecha de Elaboración")
              fecha_elaboracion_label.setFont(QFont('Arial',10))
              fecha_elaboracion_label.move(680,54)
              ##QDateTimeEdit fue utilizado para la creacion de un calendario para seleccionar la fecha segun lo que pida
              fecha_elaboracion= QDateTimeEdit(self)
              fecha_elaboracion.setCalendarPopup(True)##se muestra como verdadero  la creacion del calendario
              fecha_elaboracion.setDisplayFormat("yyyy/MM/dd")##para que en la barra se acomoden correctamente las fechas o en como va estar el formato 
              ##muestra primero el año que es "yyyy", y haci va señalando la posicion de la fechas
              fecha_elaboracion.calendarWidget().setLocale(QLocale("es_ES"))##setLocale para que el calendario este en español poniendo "es_ES"
              fecha_elaboracion.setDateTime(QDateTime.currentDateTime())##se utiliza para poder actualizar el calendario y muestre la fecha actual
              fecha_elaboracion.calendarWidget().clicked.connect(self.actualizar_fecha_hora)##se hace para poder realizar la actualizacion de dia,mes y hora
              fecha_elaboracion.dateChanged.connect(self.actualizar_anio)##aqui para actualizar el año del calendario
              fecha_elaboracion.resize(250,24)
              fecha_elaboracion.move(680,74)
       ##puesto
              puesto_cubrir_label = QLabel(self)
              puesto_cubrir_label.setText("Puesto a cubrir")
              puesto_cubrir_label.setFont(QFont('Arial',10))
              puesto_cubrir_label.move(20,104)
              
              self.puesto_cubrir_input = QComboBox(self)
              self.puesto_cubrir_input.addItems(["1","2","3"])
              self.puesto_cubrir_input.resize(910,24)
              self.puesto_cubrir_input.move(20,122)
       ##nombre y puesto de quien solicita
              nombre_label = QLabel(self)
              nombre_label.setText("Nombre y puesto de quien solicita")
              nombre_label.setFont(QFont('Arial',10))
              nombre_label.move(20,154)

              self.nombre_input = QLineEdit(self)
              self.nombre_input.resize(910,24)
              self.nombre_input.move(20,174)

       ##fecha de reclutamiento
              reclutamiento_label = QLabel(self)
              reclutamiento_label.setText("Fecha de Reclutamiento")
              reclutamiento_label.setFont(QFont('Arial',10))
              reclutamiento_label.move(20,204)

              reclutamiento = QDateTimeEdit(self)
              reclutamiento.setCalendarPopup(True)
              reclutamiento.setDisplayFormat("yyyy-MM-dd")
              reclutamiento.calendarWidget().setLocale(QLocale("es_ES"))
              reclutamiento.setDateTime(QDateTime.currentDateTime())
              reclutamiento.dateChanged.connect(self.actualizar_anio1)
              reclutamiento.resize(220,24)
              reclutamiento.move(20,224)

       ##fecha de inicio vacante
              inicio_vacante_label = QLabel(self)
              inicio_vacante_label.setText("Fecha de Inicio Vacante")
              inicio_vacante_label.setFont(QFont('Arial',10))
              inicio_vacante_label.move(260,204)
              ##creacion de otro calendario
              inicio_vacante = QDateTimeEdit(self)
              inicio_vacante.setCalendarPopup(True)
              inicio_vacante.setDisplayFormat("yyyy-MM-dd")
              inicio_vacante.calendarWidget().setLocale(QLocale("es_ES"))
              inicio_vacante.setDateTime(QDateTime.currentDateTime())
              inicio_vacante.dateChanged.connect(self.actualizar_anio2)
              inicio_vacante.resize(220,24)
              inicio_vacante.move(260,224)

       ##numero de vacante
              numero_vacante_label = QLabel(self)
              numero_vacante_label.setText("Número de Vacantes")
              numero_vacante_label.setFont(QFont('Arial',10))
              numero_vacante_label.move(500,204)

              self.numero_vacante_input = QLineEdit(self)
              self.numero_vacante_input.resize(215,24)
              self.numero_vacante_input.move(500,224)
       ##tipo de vacante
              tipo_vacante_label = QLabel(self)
              tipo_vacante_label.setText("Tipo de Vacante")
              tipo_vacante_label.setFont(QFont('Arial',10))
              tipo_vacante_label.move(730,204)

              self.tipo_vacante_input =QComboBox(self)
              self.tipo_vacante_input.addItems(["Temporal","1","2","3"])
              self.tipo_vacante_input.resize(200,24)
              self.tipo_vacante_input.move(730,224)
       ##vacante generada por:
              vacante_label = QLabel(self)
              vacante_label.setText("Vacante generada por:")
              vacante_label.setFont(QFont('Arial',10))
              vacante_label.move(20,254)

              t_label =QLabel(self)
              t_label.setText("Especifique")
              t_label.setFont(QFont('Arial',10))
              t_label.move(620,274)
              
              self.t_input = QLineEdit(self)
              self.t_input.resize(150,24)
              self.t_input.move(620,294)
              ##creacion de los botones de seleccion
              ##se utiliza la funcion QRadioButton para lograr ese tipo de button
              vacante_button1 =QRadioButton('Baja',self)##dando el nombre de el 
              vacante_button1.move(20,294)
              vacante_button2 = QRadioButton('Incapacidad',self)
              vacante_button2.move(100,294)
              vacante_button3 = QRadioButton('Licencia o Permiso',self)
              vacante_button3.move(200,294)##son las coordenadas de donde se va a localizar
              vacante_button4 = QRadioButton('Nueva Creación',self)
              vacante_button4.move(350,294)
              vacante_button5 = QRadioButton('Defunción',self)
              vacante_button5.move(470,294)
              vacante_button6 = QRadioButton('Otro',self)
              vacante_button6.move(560,294)
              ##se crean todos los button que se desean
              ##para poder conectar los buttones y se puedan seleccionar 
              vacante_button1.toggled.connect(self.on_toggle)
              ##llama a una funcion para que diga la seleccion de que button
              vacante_button2.toggled.connect(self.on_toggle)
              vacante_button3.toggled.connect(self.on_toggle)
              vacante_button4.toggled.connect(self.on_toggle)
              vacante_button5.toggled.connect(self.on_toggle)
              vacante_button6.toggled.connect(self.on_toggle)

       ##botton de enviar
              self.enviar_button = QPushButton(self)
              self.enviar_button.setText("Enviar Requisición")
              self.enviar_button.setFont(QFont('Arial',10))
              self.enviar_button.resize(120,35)
              self.enviar_button.move(20,330)
              self.enviar_button.clicked.connect(self.BDInsert)
       ##radiobutton
       def on_toggle(self):
              sender =self.sender()##esto se hace para que se realice la funcion de poder seleccionar
              if sender.isChecked():##y que cuando se seleccione se muestre por consola
                     texto = sender.text()
                     print(f'Se selecciono: {texto}')##diciendo el nombre del button que se a seleccionado
                     self.valor=texto
       ##calendario
       def actualizar_fecha_hora(self,date):##subclase para la actualizacion 
              fecha_hora_actual = self.sender().selectedDate().toDateTime(fecha_elaboracion.time())##funcion para tener el tiempo actual
              fecha_elaboracion.setDateTime(fecha_hora_actual)##se llama la variable de actualizacion para completar la funcion de tiempo actual de calendario
       def actualizar_anio(self,date):
              anio_actual =date.year()#aqui para actualizar el año
              fecha_elaboracion.setDate(date)
              fecha_elaboracion.setTime(fecha_elaboracion.time())##para complete la funcion de poner el año correctamente
       def actualizar_anio1(self,date):
              anio_actual = date.year()
              reclutamiento.setDate(date)
              reclutamiento.setTime(reclutamiento.time())
       def actualizar_anio2(self,date):
              anion_actual = date.year()
              inicio_vacante.setDate(date)
              inicio_vacante.setTime(inicio_vacante.time())
       ##se hacen subclases diferentes de actualizar año ya que cada calendario tiene diferente funcion, al no tener la misma fecha , la seleccion es de direntes fechas
       ##si se pone en una sola clase todos no se podran cambiar las fechas en todas las barras se pondra la misma fecha por eso se hacen en diferentes subclases pero la misma funcion 
       def mostrar_ventana(self):
              print("Mostrar vtn")

       def BDInsert(self):
              folio = self.folio_input.text()
              area = self.area_solicita_input.currentText()
              fe = fecha_elaboracion.date().toString("yyyy-MM-dd")
              puesto = self.puesto_cubrir_input.currentText()
              nps = self.nombre_input.text()
              fr = reclutamiento.date().toString("yyyy-MM-dd")
              fi = inicio_vacante.date().toString("yyyy-MM-dd")
              nv = self.numero_vacante_input.text()
              tv = self.tipo_vacante_input.currentText()
              vgp = self.valor

              sql = "SELECT folio FROM requisicion WHERE folio = %s"
              con_db.cursor.execute(sql, (folio,))
              result = con_db.cursor.fetchone()
              if result is None:
                     print("Añadir")
                     sql = "INSERT INTO requisicion (v_gene_por, tipo_vacante_id, autorizacion_id, puesto_id, areas_id, med_public_id, folio, fechaEla, nombre, puesto, area, fechaReclu, fechaInicio, num_vacantes ) VALUES (%s, %s, %s,%s, %s, %s, %s, %s, %s,%s, %s, %s,%s, %s)"
                     values = (1, 1, 1, 1, 1, 1, folio, fe, nps, puesto, area, fr, fi, nv )
                     con_db.cursor.execute(sql, values)
                     con_db.comit()
                     print("Se pudo")
                     #Se indica si el registro fue exitoso
                     print("requisitos añadidos correctamente.")
              else:
                     print("Ya existe")

if __name__ == '__main__':
       with open('styles.css', 'r') as f:
              style = f.read()
       app = QApplication(sys.argv)##administrar todo lo que se haga en la venta
       app.setStyleSheet(style)    
       ventana = vtn()
       sys.exit(app.exec())#salir
