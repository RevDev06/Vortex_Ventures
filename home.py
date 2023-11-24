import sys
from PyQt6.QtWidgets import (QApplication, QWidget,QLabel,QMainWindow)#type: ignore
from PyQt6.QtGui import QFont,QAction#type: ignore
from PyQt6.QtCore import pyqtSignal#type: ignore
from requisicion import vtn 
from analisis import v

class HomeWindow(QMainWindow):
    abrir_ventana = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Home")
        screen_geometry = QApplication.primaryScreen().availableGeometry()
        window_width = 1000
        window_height = 600
        window_x = (screen_geometry.width() - window_width) // 2
        window_y = (screen_geometry.height() - window_height) // 2
        self.setGeometry(window_x, window_y, window_width, window_height)

        self.company_name = QLabel("VORTEX VENTURES", self)
        self.company_name.setGeometry(20, 30, 120, 20)
        self.create_navigation_bar()


    def create_navigation_bar(self):
        menu_bar = self.menuBar()
        menu_bar.move(50,50)
##nombre de la barra
        file_contratacion = menu_bar.addMenu("&Contratación")
##puesto
        action_p =QAction("&PUESTO",self)
        action_p.triggered.connect(self.redirect_to_window)
        file_contratacion.addMenu("action_p")
##requisicion
        action_requisicion = QAction("&REQUISICION",self)
        action_requisicion.triggered.connect(self.requisicion)
        file_contratacion.addAction(action_requisicion)
##antorizacion
        action_aut = QAction("&AUTORIZACION",self)
        action_aut.triggered.connect(self.redirect_to_window)
        file_contratacion.addAction(action_aut)
##vacantes
        action_vac = QAction("&VACANTES",self)
        action_vac.triggered.connect(self.redirect_to_window)
        file_contratacion.addAction(action_vac)
##candidatos
        action_can = QAction("&CANDIDATOS",self)
        action_can.triggered.connect(self.redirect_to_window)
        file_contratacion.addAction(action_can)
       
        file_catalogos = menu_bar.addMenu("&Catalogos")
#area
        action_a = QAction("&CANDIDATOS",self)
        action_a.triggered.connect(self.redirect_to_window)
        file_catalogos.addAction(action_a)
#carrera
        action_ca = QAction("&AREA",self)
        action_ca.triggered.connect(self.redirect_to_window)
        file_catalogos.addAction(action_ca)
#escolaridad
        action_esc = QAction("&CESCOLARIDAD",self)
        action_esc.triggered.connect(self.redirect_to_window)
        file_catalogos.addAction(action_esc)
##estado civil
        action_ec = QAction("&ESTADO CIVIL",self)
        action_ec.triggered.connect(self.redirect_to_window)
        file_catalogos.addAction(action_ec)
#grado de avance
        action_ga = QAction("&GRADO DE AVANCE",self)
        action_ga.triggered.connect(self.redirect_to_window)
        file_catalogos.addAction(action_ga)
##habilidades
        action_ha = QAction("&HABILIDADES",self)
        action_ha.triggered.connect(self.redirect_to_window)
        file_catalogos.addAction(action_ha)
##idioma
        action_id = QAction("&IDIOMA",self)
        action_id.triggered.connect(self.redirect_to_window)
        file_catalogos.addAction(action_id)
##medio de publicidad
        action_mp = QAction("&MEDIO DE PUBLICIDAD",self)
        action_mp.triggered.connect(self.redirect_to_window)
        file_catalogos.addAction(action_mp)
##documentos solicitados
        action_ds = QAction("&DOCUMENTOS SOLICITADOS",self)
        action_ds.triggered.connect(self.redirect_to_window)
        file_catalogos.addAction(action_ds)
        
        
    def requisicion(self):
        # Logica para enviar a otras ventanas
        if not hasattr(self, 'vtn_requisicion'):
            self.vtn_requisicion = vtn()
            self.vtn_requisicion.show()
            self.close()
        else:
            self.show()
##se crea subclases para la coneccion de ventanas para cada boton
    def redirect_to_window(self):
        self.vtn_analisis = v()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    home_window = HomeWindow()
    home_window.show()
    sys.exit(app.exec())
    
