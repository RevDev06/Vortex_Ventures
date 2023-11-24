import sys
from PyQt6.QtWidgets import (QApplication, QWidget,QLabel,QMainWindow)#type: ignore
from PyQt6.QtGui import QFont,QAction#type: ignore
from PyQt6.QtCore import pyqtSignal#type: ignore
from requisicion import vtn 

class HomeWindow(QMainWindow):
    abrrir_ventana = pyqtSignal()
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
##button
        navigation_bar = self.addToolBar("Navigation Bar")
        action = QAction(self)
        action.triggered.connect(self.redirect_to_window)
        action.setCheckable(True)
        navigation_bar.addAction(action)

        action1 = QAction(self)
        action1.triggered.connect(self.redirect_to_window)
        action1.setCheckable(True)
        navigation_bar.addAction(action1)
##nombre de la barra
        cn = self.menuBar()
        file_contratacion = cn.addMenu("&Contratación")
        file_puesto=file_contratacion.addMenu("PUESTO")
        file_re=file_contratacion.addMenu("REQUISICION")
        file_aut=file_contratacion.addMenu("AUTORIZACION")
        file_vct=file_contratacion.addMenu("VACANTES")
        file_can=file_contratacion.addMenu("CANDIDATOS")
        file_puesto.addAction(action)
        file_re.addAction(action)
        file_aut.addAction(action)
        file_vct.addAction(action)
        file_can.addAction(action)
        file_ventas = cn.addMenu("&Catalogos")
        file_a=file_ventas.addMenu("AREA")
        file_cr=file_ventas.addMenu("CARRERA")
        file_e=file_ventas.addMenu("ESCOLORIDAD")
        file_ec=file_ventas.addMenu("ESTADO CIVIL")
        file_ga=file_ventas.addMenu("GRADO DE AVANCE")
        file_hb=file_ventas.addMenu("HABILIDADES")
        file_id=file_ventas.addMenu("IDIOMA")
        file_mp=file_ventas.addMenu("MEDIO DE PUBLICIDAD")
        file_s=file_ventas.addMenu("DOCUMENTOS SOLICITADOS")
        file_a.addAction(action1)
        file_cr.addAction(action1)
        file_e.addAction(action1)
        file_ec.addAction(action1)
        file_ga.addAction(action1)
        file_hb.addAction(action1)
        file_id.addAction(action1)
        file_mp.addAction(action1)
        file_s.addAction(action1)
        
        action_requisicion = QAction(self)
        action_requisicion.triggered.connect(self.abrrir_ventana.emit)
        file_re.addAction(action_requisicion)


    def redirect_to_window(self):
        # Logica para enviar a otras ventanas
        self.close()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    home_window = HomeWindow()
    vtn=vtn()
    home_window.abrrir_ventana.connect(vtn.show)
    home_window.abrrir_ventana.connect(home_window.redirect_to_window)
    home_window.show()
    sys.exit(app.exec())
    
