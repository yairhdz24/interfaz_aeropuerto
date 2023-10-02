from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from aeropuerto import Aeropuerto
from vuelo import Vuelo

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.aeropuerto = Aeropuerto()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.agregar_inicio_pushButton.clicked.connect(lambda: (self.click_agregar(True)))
        self.ui.agregar_final_pushButton.clicked.connect(lambda: (self.click_agregar(False)))
        self.ui.mostrar_pushButton.clicked.connect(self.click_mostrar)
        self.ui.mostrar_tabla_pushButton.clicked.connect(self.mostrar_Tabla)
        self.ui.buscar_pushButton.clicked.connect(self.buscar_id)

        self.ui.actionAbrir.triggered.connect(self.action_Abrir_Archivo)
        self.ui.actionGuardar.triggered.connect(self.action_Guardar_Archivo)

    @Slot()
    def click_agregar(self, where:bool):        
        id = self.ui.id_lineEdit.text()
        origen = self.ui.origen_lineEdit.text()
        destino = self.ui.destino_lineEdit.text()
        peso = self.ui.peso_spinBox.value()

        myVuelo = Vuelo(id, origen, destino, peso)
        if where:
            self.aeropuerto.agregar_inicio(myVuelo)
        else:
            self.aeropuerto.agregar_final(myVuelo)

        #print(id, origen, destino, peso)
        #self.ui.salida.insertPlainText(id + origen + destino + str(peso))

    @Slot()
    def click_mostrar(self):
        self.ui.salida.clear()
        self.ui.salida.insertPlainText(str(self.aeropuerto))

    @Slot()
    def action_Abrir_Archivo(self):
        ubicacion = QFileDialog.getOpenFileName(
             self,
            'Abrir Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        if self.aeropuerto.abrir(ubicacion):
            QMessageBox.information(
                self,
                "Exito",
                "Se abrio el archivo correctamenet :D")
            
            self.click_mostrar() #muestra automaticamente
            self.mostrar_Tabla()
            
        else:
            QMessageBox.information(
                self,
                "Error", 
                "No se pudo abrir el archivo ;( ")
        

    @Slot()
    def action_Guardar_Archivo(self):
        ubicacion = QFileDialog.getSaveFileName(
             self,
            'Guardar Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        if self.aeropuerto.guardar(ubicacion):
            QMessageBox.information(
        self,
        "Exito",
       "Archivo Guardado exitosamente :D" )
        else:
            QMessageBox.information(
        self,
        "Error",
        "No se pudo guardar el archivo :C" )

    @Slot()
    def mostrar_Tabla(self):
        #print("Mostrar tablaAaa")
        self.ui.tabla.setColumnCount(4) # numero de columnas
        headers = ["ID", "Origen", "Destino", "Peso"]
        self.ui.tabla.setHorizontalHeaderLabels(headers)

        self.ui.tabla.setRowCount(len(self.aeropuerto))

        row = 0
        for vuelo in self.aeropuerto:
            id_widget = QTableWidgetItem(vuelo.id)
            origen_widget = QTableWidgetItem(vuelo.origen)
            destino_widget = QTableWidgetItem(vuelo.destino)
            peso_widget = QTableWidgetItem(str(vuelo.peso))

            self.ui.tabla.setItem(row, 0, id_widget)
            self.ui.tabla.setItem(row, 1, origen_widget)
            self.ui.tabla.setItem(row, 2, destino_widget)
            self.ui.tabla.setItem(row, 3, peso_widget)

            row += 1

    @Slot()
    def buscar_id(self):
        id = self.ui.buscar_lineEdit.text()
        
        encontrado = False
        for vuelo in self.aeropuerto:
            if id == vuelo.id:
                self.ui.tabla.clear()
                self.ui.tabla.setColumnCount(4)  # numero de columnas
                headers = ["ID", "Origen", "Destino", "Peso"]
                self.ui.tabla.setHorizontalHeaderLabels(headers)
                self.ui.tabla.setRowCount(1)

                id_widget = QTableWidgetItem(vuelo.id)
                origen_widget = QTableWidgetItem(vuelo.origen)  
                destino_widget = QTableWidgetItem(vuelo.destino)  
                peso_widget = QTableWidgetItem(str(vuelo.peso))

                self.ui.tabla.setItem(0, 0, id_widget)                 
                self.ui.tabla.setItem(0, 1, origen_widget)                  
                self.ui.tabla.setItem(0, 2, destino_widget)                 
                self.ui.tabla.setItem(0, 3, peso_widget)  

                encontrado = True
                return                                                                                                                                     
            
        if not encontrado:
            QMessageBox.warning(
                self,
                "Atencion",
                f"El Avion con el ID: {id} no fue encontrado ;("
            )               
            

    