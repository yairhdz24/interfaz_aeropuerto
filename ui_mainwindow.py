# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(680, 557)
        MainWindow.setTabletTracking(False)
        MainWindow.setStyleSheet(u"\n"
"\n"
"/* Estilo para el t\u00edtulo del QGroupBox */\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 10px; /* Ajusta el espaciado alrededor del t\u00edtulo */\n"
"}\n"
"\n"
"/* Estilo para Bot\u00f3n (QPushButton) */\n"
"QPushButton {\n"
"    background-color: #1e6091; /* Azul oscuro para el fondo */\n"
"    color: white; /* Color del texto */\n"
"    border: 2px solid #1e6091; /* Borde con color */\n"
"    border-radius: 5px; /* Bordes redondeados */\n"
"    padding: 5px 10px; /* Espaciado interno */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2980b9; /* Color de fondo en hover */\n"
"    border: 2px solid #2980b9; /* Borde en hover */\n"
"}\n"
"\n"
"QSpinBox {\n"
"    background-color: #ecf0f1; /* Color de fondo */\n"
"    border: 1px solid #bdc3c7; /* Borde con color */\n"
"    border-radius: 3px; /* Bordes redondeados */\n"
"    padding: 2px; /* Espaciado interno */\n"
"    color: #333; /* Color del texto */\n"
"}\n"
""
                        "\n"
"QTabBar::tab {\n"
"                background: #0074D9;\n"
"                color: #FFFFFF;\n"
"                padding: 5px 10px;\n"
"                border: 1px solid #0056b3;\n"
"                border-top-left-radius: 5px;\n"
"                border-top-right-radius: 5px;\n"
"            }\n"
" \n"
"QTabBar::tab:selected {\n"
"                background: #0056b3;\n"
" }\n"
"\n"
"QMessageBox {\n"
"    background-color: #FFFFFF; /* Color de fondo */\n"
"}\n"
"\n"
"QMessageBox QLabel {\n"
"    color: #333333; /* Color del texto del mensaje */\n"
"}\n"
"\n"
"QMessageBox QPushButton {\n"
"    background-color: #0074D9; /* Color del bot\u00f3n */\n"
"    color: #FFFFFF; /* Color del texto del bot\u00f3n */\n"
"    border: 1px solid #0056b3; /* Borde del bot\u00f3n */\n"
"    border-radius: 5px; /* Bordes redondeados */\n"
"    padding: 5px 10px; /* Espaciado interno del bot\u00f3n */\n"
"}\n"
"\n"
"QMessageBox QPushButton:hover {\n"
"    background-color: #0056b3; /* Cambiar color de fondo al pasar el rat\u00f3"
                        "n */\n"
"}\n"
"\n"
"")
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.vuelo_groupBox = QGroupBox(self.tab)
        self.vuelo_groupBox.setObjectName(u"vuelo_groupBox")
        self.gridLayout = QGridLayout(self.vuelo_groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.peso_label = QLabel(self.vuelo_groupBox)
        self.peso_label.setObjectName(u"peso_label")

        self.gridLayout.addWidget(self.peso_label, 3, 0, 1, 1)

        self.agregar_final_pushButton = QPushButton(self.vuelo_groupBox)
        self.agregar_final_pushButton.setObjectName(u"agregar_final_pushButton")

        self.gridLayout.addWidget(self.agregar_final_pushButton, 6, 1, 1, 1)

        self.origen_label = QLabel(self.vuelo_groupBox)
        self.origen_label.setObjectName(u"origen_label")

        self.gridLayout.addWidget(self.origen_label, 1, 0, 1, 1)

        self.destino_label = QLabel(self.vuelo_groupBox)
        self.destino_label.setObjectName(u"destino_label")

        self.gridLayout.addWidget(self.destino_label, 2, 0, 1, 1)

        self.destino_lineEdit = QLineEdit(self.vuelo_groupBox)
        self.destino_lineEdit.setObjectName(u"destino_lineEdit")

        self.gridLayout.addWidget(self.destino_lineEdit, 2, 1, 1, 2)

        self.id_label = QLabel(self.vuelo_groupBox)
        self.id_label.setObjectName(u"id_label")

        self.gridLayout.addWidget(self.id_label, 0, 0, 1, 1)

        self.agregar_inicio_pushButton = QPushButton(self.vuelo_groupBox)
        self.agregar_inicio_pushButton.setObjectName(u"agregar_inicio_pushButton")

        self.gridLayout.addWidget(self.agregar_inicio_pushButton, 6, 0, 1, 1)

        self.id_lineEdit = QLineEdit(self.vuelo_groupBox)
        self.id_lineEdit.setObjectName(u"id_lineEdit")

        self.gridLayout.addWidget(self.id_lineEdit, 0, 1, 1, 2)

        self.origen_lineEdit = QLineEdit(self.vuelo_groupBox)
        self.origen_lineEdit.setObjectName(u"origen_lineEdit")

        self.gridLayout.addWidget(self.origen_lineEdit, 1, 1, 1, 2)

        self.mostrar_pushButton = QPushButton(self.vuelo_groupBox)
        self.mostrar_pushButton.setObjectName(u"mostrar_pushButton")

        self.gridLayout.addWidget(self.mostrar_pushButton, 6, 2, 1, 1)

        self.peso_spinBox = QSpinBox(self.vuelo_groupBox)
        self.peso_spinBox.setObjectName(u"peso_spinBox")

        self.gridLayout.addWidget(self.peso_spinBox, 3, 2, 1, 1)


        self.gridLayout_2.addWidget(self.vuelo_groupBox, 0, 0, 1, 1)

        self.salida = QPlainTextEdit(self.tab)
        self.salida.setObjectName(u"salida")

        self.gridLayout_2.addWidget(self.salida, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_4 = QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.tabla = QTableWidget(self.tab_2)
        self.tabla.setObjectName(u"tabla")

        self.gridLayout_4.addWidget(self.tabla, 0, 0, 1, 3)

        self.buscar_lineEdit = QLineEdit(self.tab_2)
        self.buscar_lineEdit.setObjectName(u"buscar_lineEdit")

        self.gridLayout_4.addWidget(self.buscar_lineEdit, 1, 0, 1, 1)

        self.buscar_pushButton = QPushButton(self.tab_2)
        self.buscar_pushButton.setObjectName(u"buscar_pushButton")

        self.gridLayout_4.addWidget(self.buscar_pushButton, 1, 1, 1, 1)

        self.mostrar_tabla_pushButton = QPushButton(self.tab_2)
        self.mostrar_tabla_pushButton.setObjectName(u"mostrar_tabla_pushButton")

        self.gridLayout_4.addWidget(self.mostrar_tabla_pushButton, 1, 2, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 680, 21))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)
        self.menuArchivo.addSeparator()

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.vuelo_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"VUELO", None))
        self.peso_label.setText(QCoreApplication.translate("MainWindow", u"Peso:", None))
        self.agregar_final_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar final", None))
        self.origen_label.setText(QCoreApplication.translate("MainWindow", u"Origen:", None))
        self.destino_label.setText(QCoreApplication.translate("MainWindow", u"Destino:", None))
        self.id_label.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.agregar_inicio_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar inicio", None))
        self.mostrar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.buscar_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ID de Vuelo", None))
        self.buscar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.mostrar_tabla_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tabla", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

