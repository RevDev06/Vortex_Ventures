import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from requisicion import vtn 
from analisis import v
from area_catalogo import VArea
from carrera_catalogo import Vcarrera
from documentossoli_catalogo import Vdocumentossoli
from escolaridad_catalogo import Vescolaridad
from estadocivil_catalogo import Vestadocivil
from gradoavance_catalogo import Vgradoavnce
from habilidades_catalogo import Vhabilidad
from idioma_catalogo import Vidioma
from mediopb_catalogo import Vmediopb

class HomeWindow(QMainWindow):
    abrir_ventana = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        self.setWindowTitle("Home")
        screen_geometry = QApplication.primaryScreen().availableGeometry()
        window_width = 1000
        window_height = 600
        window_x = (screen_geometry.width() - window_width) // 2
        window_y = (screen_geometry.height() - window_height) // 2
        self.setGeometry(window_x, window_y, window_width, window_height)

        self.company_name = QLabel("VORTEX VENTURES", self)
        self.company_name.setFont(QFont('Bookman Old Style',40))
        self.company_name.setGeometry(250, 370, 600, 50)
        self.create_navigation_bar()

        gradient = QLinearGradient(0, self.height(), 0, 0)
        gradient.setColorAt(0, QColor("#0a0908"))  # Color más oscuro en la parte inferior
        gradient.setColorAt(0.25, QColor("#11212d"))
        gradient.setColorAt(0.5, QColor("#3d4d55"))
        gradient.setColorAt(0.75, QColor("#5e503f"))  # Color más claro en la parte superior
        gradient.setColorAt(1, QColor("#171614")) 
        # Establecer el degradado como fondo de la ventana
        palette = self.palette()
        palette.setBrush(QPalette.ColorGroup.All, QPalette.ColorRole.Window, QBrush(gradient))
        self.setPalette(palette)

        palette = self.palette()
        palette.setBrush(QPalette.ColorGroup.All, QPalette.ColorRole.Window, QBrush(gradient))


    def create_navigation_bar(self):
        menu_bar = self.menuBar()
        menu_bar.setFixedHeight(40)

        self.close_button = QPushButton("X", self)
        self.close_button.clicked.connect(self.close)
        self.close_button.setGeometry(960, 0, 40, 40)
        self.close_button.setStyleSheet("background-color:#5f5a4d; color:#ccc6ac;border-radius: 5px;")


        self.minimize_button = QPushButton("-", self)
        self.minimize_button.clicked.connect(self.showMinimized)
        self.minimize_button.setGeometry(920, 0, 40, 40)
        self.minimize_button.setStyleSheet("background-color:#867c61; color:#ccc6ac;border-radius: 5px;")

##nombre de la barra
        file_contratacion = menu_bar.addMenu("&CONTRATACIÓN")
        file_contratacion.setFont(QFont('Arial',9))
##puesto
        action_p = QAction("&PUESTO",self)
        action_p.triggered.connect(self.redirect_to_window)
        file_contratacion.addAction(action_p)
##requisicion
        action_requisicion = QAction("&REQUISICION",self)
        action_requisicion.triggered.connect(self.requisicion)
        file_contratacion.addAction(action_requisicion)
##antorizacion
        action_aut = QAction("&AUTORIZACION",self)
        action_aut.triggered.connect(self.analisis)
        file_contratacion.addAction(action_aut)
##vacantes
        action_vac = QAction("&VACANTES",self)
        action_vac.triggered.connect(self.redirect_to_window)
        file_contratacion.addAction(action_vac)
##candidatos
        action_can = QAction("&CANDIDATOS",self)
        action_can.triggered.connect(self.redirect_to_window)
        file_contratacion.addAction(action_can)
       
        file_catalogos = menu_bar.addMenu("&CATALOGOS")
        file_catalogos.setFont(QFont('Arial',9))
#area
        action_a = QAction("&CANDIDATOS",self)
        action_a.triggered.connect(self.redirect_to_window)
        file_catalogos.addAction(action_a)
#carrera
        action_ca = QAction("&AREA",self)
        action_ca.triggered.connect(self.area)
        file_catalogos.addAction(action_ca)
#escolaridad
        action_esc = QAction("&CESCOLARIDAD",self)
        action_esc.triggered.connect(self.escolaridad)
        file_catalogos.addAction(action_esc)
##estado civil
        action_ec = QAction("&ESTADO CIVIL",self)
        action_ec.triggered.connect(self.estadocivil)
        file_catalogos.addAction(action_ec)
#grado de avance
        action_ga = QAction("&GRADO DE AVANCE",self)
        action_ga.triggered.connect(self.gradoavance)
        file_catalogos.addAction(action_ga)
##habilidades
        action_ha = QAction("&HABILIDADES",self)
        action_ha.triggered.connect(self.habilidades)
        file_catalogos.addAction(action_ha)
##idioma
        action_id = QAction("&IDIOMA",self)
        action_id.triggered.connect(self.idioma)
        file_catalogos.addAction(action_id)
##medio de publicidad
        action_mp = QAction("&MEDIO DE PUBLICIDAD",self)
        action_mp.triggered.connect(self.mediopb)
        file_catalogos.addAction(action_mp)
##documentos solicitados
        action_ds = QAction("&DOCUMENTOS SOLICITADOS",self)
        action_ds.triggered.connect(self.documentossoli)
        file_catalogos.addAction(action_ds)
        
    def requisicion(self):
        # Logica para enviar a otras ventanas
        if not hasattr(self, 'vtn_requisicion'):
            self.vtn_requisicion = vtn()
            self.vtn_requisicion.show()
            self.close()
        else:
            self.show()

    def analisis(self):
        if not hasattr(self,'v_analisis'):
            self.v_analisis=v()
            self.v_analisis.show()
            self.close()
        else:
            self.show()

    def area(self):
        if not hasattr(self,'v_area'):
            self.v_area=VArea()
            self.v_area.show()
            self.close()
        else:
            self.show()
    def carrera(self):
        if not hasattr(self,'v_carrera'):
            self.v_carrera = Vcarrera()
            self.v_carrera.show()
            self.close()
        else:
            self.show()
    def documentossoli(self):
        if not hasattr(self,'v_soli'):
            self.v_soli = Vdocumentossoli()
            self.v_soli.show()
            self.close()
        else:
            self.show()
    def escolaridad(self):
        if not hasattr(self,'v_esc'):
            self.v_esc = Vescolaridad()
            self.v_esc.show()
            self.close()
        else:
            self.show()
    def estadocivil(self):
        if not hasattr(self,'v_ec'):
            self.v_ec = Vestadocivil()
            self.v_ec.show()
            self.close()
        else:
            self.show()
    def gradoavance(self):
        if not hasattr(self,'v_ga'):
            self.v_ga = Vgradoavnce()
            self.v_ga.show()
            self.close()
        else:
            self.show()
    def habilidades(self):
        if not hasattr(self,'v_ha'):
            self.v_ha = Vhabilidad()
            self.v_ha.show()
            self.close()
        else:
            self.show()
    def idioma(self):
        if not hasattr(self,'v_idm'):
            self.v_idm = Vidioma()
            self.v_idm.show()
            self.close()
        else:
            self.show()
    def mediopb(self):
        if not hasattr(self,'v_pb'):
            self.v_pb = Vmediopb()
            self.v_pb.show()
            self.close()
        else:
            self.show()

    def redirect_to_window(self):
        self.vtn_catalogos
        
    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
        self.dragPos = event.globalPosition().toPoint()
        event.accept()

if __name__ == "__main__":
    with open('styles.css', 'r') as f:
        style = f.read()
    app = QApplication(sys.argv)
    app.setStyleSheet(style) 
    home_window = HomeWindow()
    home_window.show()
    sys.exit(app.exec())
    
