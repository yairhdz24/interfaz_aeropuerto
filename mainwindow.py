from PySide2.QtWidgets import QMainWindow
from ui_mainwindow import Ui_MainWindow  
from PySide2.QtCore import Slot
from aeropuerto import Aeropuerto
from vuelo import Vuelo

class MainWindow (QMainWindow):
    def __init__(self):                     #reservar memoria para ventana
        super(MainWindow, self).__init__()  #llamamos el constructor para reservar memoria
        
        self.aeropuerto = Aeropuerto() #creamos el objeto del vuelo
        
        self.ui = Ui_MainWindow() 
        self.ui.setupUi(self)
        
        self.ui.agregar_final_pushButton.clicked.connect(self.click_agregar_Final)
        self.ui.agregar_inicio_pushButton.clicked.connect(self.click_agregar_Inicio)
        self.ui.mostar_pushButton.clicked.connect(self.click_mostrar)
        
    @Slot()
    def click_agregar_Final(self):
        id = self.ui.ID_lineEdit.text()
        origen = self.ui.ORIGEN_lineEdit.text()
        destino = self.ui.DESTINO_lineEdit.text()
        peso = self.ui.PESO_spinBox.value()
        
        vuelo = Vuelo(id, origen, destino, peso)
        self.aeropuerto.agregar_final(vuelo)
        #self.ui.salida.insertPlainText(vuelo)
        
    @Slot()
    def click_agregar_Inicio(self):
        id = self.ui.ID_lineEdit.text()
        origen = self.ui.ORIGEN_lineEdit.text()
        destino = self.ui.DESTINO_lineEdit.text()
        peso = self.ui.PESO_spinBox.value()
        
        vuelo = Vuelo(id, origen, destino, peso)
        self.aeropuerto.agregar_inicio(vuelo)
        
        
    @Slot()
    def click_mostrar(self):
        self.ui.salida.clear()  # Limpia el campo de salida antes de mostrar los datos
        vuelo = str(self.aeropuerto)
        #self.aeropuerto.mostrar()
        self.ui.salida.insertPlainText(vuelo)
        #self.ui.mostrar.insertPlainText(str(self.aeropuerto.mostrar()))
        
   
   