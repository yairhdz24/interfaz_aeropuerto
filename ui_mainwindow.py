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
        MainWindow.resize(632, 382)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayout = QFormLayout(self.centralwidget)
        self.formLayout.setObjectName(u"formLayout")
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)

        self.DESTINO_lineEdit = QLineEdit(self.groupBox_2)
        self.DESTINO_lineEdit.setObjectName(u"DESTINO_lineEdit")

        self.gridLayout.addWidget(self.DESTINO_lineEdit, 2, 1, 1, 2)

        self.mostar_pushButton = QPushButton(self.groupBox_2)
        self.mostar_pushButton.setObjectName(u"mostar_pushButton")

        self.gridLayout.addWidget(self.mostar_pushButton, 5, 2, 1, 1)

        self.PESO_spinBox = QSpinBox(self.groupBox_2)
        self.PESO_spinBox.setObjectName(u"PESO_spinBox")

        self.gridLayout.addWidget(self.PESO_spinBox, 3, 2, 1, 1)

        self.agregar_inicio_pushButton = QPushButton(self.groupBox_2)
        self.agregar_inicio_pushButton.setObjectName(u"agregar_inicio_pushButton")

        self.gridLayout.addWidget(self.agregar_inicio_pushButton, 5, 1, 1, 1)

        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)

        self.ORIGEN_lineEdit = QLineEdit(self.groupBox_2)
        self.ORIGEN_lineEdit.setObjectName(u"ORIGEN_lineEdit")

        self.gridLayout.addWidget(self.ORIGEN_lineEdit, 1, 1, 1, 2)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 2)

        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 2, 0, 1, 1)

        self.ID_lineEdit = QLineEdit(self.groupBox_2)
        self.ID_lineEdit.setObjectName(u"ID_lineEdit")

        self.gridLayout.addWidget(self.ID_lineEdit, 0, 1, 1, 2)

        self.agregar_final_pushButton = QPushButton(self.groupBox_2)
        self.agregar_final_pushButton.setObjectName(u"agregar_final_pushButton")

        self.gridLayout.addWidget(self.agregar_final_pushButton, 5, 0, 1, 1)


        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.groupBox_2)

        self.salida = QPlainTextEdit(self.centralwidget)
        self.salida.setObjectName(u"salida")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.salida)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 632, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"VUELO", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Origen:", None))
        self.mostar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostar", None))
        self.agregar_inicio_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar Inicio", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Peso:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Destino:", None))
        self.agregar_final_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar al Final", None))
    # retranslateUi

