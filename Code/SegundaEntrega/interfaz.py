import time
from Plant_Parameter import Plant, Parameter
from Heap import MinHeap
from HashMap import PolyHash
from Queue import Queue
from linkedlist import LinkedList


from PyQt5 import QtCore, QtGui, QtWidgets #La libreria PyQt5 aporta los elementos para la interfaz grafica.
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QLabel, QLineEdit, QMessageBox
from PyQt5.QtGui import QFont, QIcon, QColor, QPixmap #QPixmap se anexa para permitir el manejo de imagenes del modulo de servicios
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QDialog, QPushButton, QTableWidget,
                             QTableWidgetItem, QAbstractItemView, QHeaderView, QMenu,
                             QActionGroup, QAction, QMessageBox, QRadioButton, QVBoxLayout, QWidget)
#####
hashmap = PolyHash()
hashmap.Primo_Polynomial()


tasks = MinHeap(24)
l_list = LinkedList()
hour = -1
##NO BORRAR NO BORRAR NO BORRAR NO BORRARNO BORRAR NO BORRAR NO BORRAR NO BORRARNO BORRAR NO BORRAR NO BORRAR NO BORRAR

##NO BORRAR NO BORRAR NO BORRAR NO BORRARNO BORRAR NO BORRAR NO BORRAR NO BORRARNO BORRAR NO BORRAR NO BORRAR NO BORRARNO BORRAR NO BORRAR NO BORRAR NO BORRAR
##ventana principal
class Ui_MainWindow(object):   

    def openWindow(self):
        self.Registrar_Planta.exec_()

    def openWindow2(self):
        self.Editor_Planta.exec_()
    
    def AbrirPedirServicios(self):#Esta funcion se ejecuta al ser clicado "pushButton_5 " y ejecuta la ventana pedirservicio
        self.pedirservicio.exec_()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("PLANTERA")
        MainWindow.resize(521, 285)
        MainWindow.setStyleSheet("background-color: rgb(131, 255, 74);\n"
"") 
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.Registrar_Planta = Registrar_Planta()

        self.Editor_Planta = Editar_Planta()
        self.pedirservicio = Notificacion()
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 90, 211, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.openWindow)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 10, 171, 71))
        font = QtGui.QFont()
        font.setFamily("Goudy Old Style")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 140, 211, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_2.clicked.connect(self.openWindow2)
        

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(150, 190, 211, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_3.clicked.connect(self.AbrirPedirServicios)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 521, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Plantera"))
        self.pushButton.setText(_translate("MainWindow", "AÑADIR PLANTAS"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ffffff;\">¡DI HOLA </span></p><p align=\"center\"><span style=\" font-weight:600; color:#ffffff;\">A PLANTERA!</span></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "EDITAR PLANTAS"))
        self.pushButton_3.setText(_translate("MainWindow", "NOTIFICACIONES"))

####### 1 ventana
class Registrar_Planta(QDialog): #Esta clase define todos los parámetros de la ventana Registrocliente
    global hashmap
    def AbrirRegistrarCliente(self):#Esta función se ejecuta al ser clicado "pushButton" y ejecuta la ventana registrocliente
        self.registrocliente.exec_()

    def Confirmation(self):
        
        plant_Name = self.textEdit.toPlainText()
        planta1 = Plant(plant_Name)
        for i in self.registrocliente.parametros:
            i.Plant = planta1
            tasks.Insert(i)
            planta1.pushBack(i)
        self.registrocliente.parametros = []
        self.textEdit.clear()

        hashmap.Insert(planta1)
        print(hashmap.Hashtable)
        self.msg = QtWidgets.QMessageBox()
        self.msg.setInformativeText("Planta agregada")
        self.msg.show()
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setWindowTitle("Notificacion")
    def __init__(self):
        QDialog.__init__(self)
        self.resize(452, 244)
        self.setWindowTitle("Registro cliente")

        self.textEdit = QtWidgets.QTextEdit(self)
        self.textEdit.setGeometry(QtCore.QRect(10, 40, 431, 31))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setText("Nombre Planta")
        self.setWindowTitle("Registro planta")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(100, 10, 271, 16))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton4 = QtWidgets.QPushButton(self)
        self.pushButton4.setGeometry(QtCore.QRect(100, 140, 241, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.pushButton4.setFont(font)
        self.pushButton4.setStyleSheet("background-color: rgb(151, 255, 66)")
        self.pushButton4.setObjectName("pushButton4")

        self.pushButton4.clicked.connect(self.AbrirRegistrarCliente)

        self.label_2.setText("Ingresar el nombre de la planta")
        self.pushButton4.setText("AÑADIR PARAMETROS")
        self.botonAgregar = QtWidgets.QPushButton(self)
        self.botonAgregar.setGeometry(QtCore.QRect(100, 90, 241, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.botonAgregar.setFont(font)
        self.botonAgregar.setStyleSheet("background-color: rgb(151, 255, 66)")
        self.botonAgregar.setObjectName("botonAgregar")
        self.botonAgregar.setText("AGREGAR LA PLANTA")
        self.botonAgregar.clicked.connect(self.Confirmation)

        self.registrocliente = Parametros()



class Parametros(QDialog):
    global hour
    def Cuenta_Parametros(self):

        Plant1 = Plant("planta temporal")
        
        parameter_1 = Parameter(self.lineEdit.text(), 
                            self.LineEdit2.text(),
                            int(self.LineEdit2.text()) + hour, Plant1)
        print(parameter_1)
        self.parametros.append(parameter_1)
        print(self.parametros)
        self.lineEdit.clear()
        self.LineEdit2.clear()
        
        #tasks.Insert(parameter_1)
    def Confirmation(self):
        self.msg = QtWidgets.QMessageBox()
        self.msg.setInformativeText("Parametro ingresado")
        self.msg.show()
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setWindowTitle("Notificacion")
        

    
    def __init__(self):
        
        self.parametros = []
        QDialog.__init__(self)
        self.resize(294, 404)
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(40, 70, 221, 41))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 271, 16))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(70, 130, 271, 16))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(11)
        self.LineEdit2 = QtWidgets.QLineEdit(self)
        self.LineEdit2.setGeometry(QtCore.QRect(40, 150, 221, 41))
        self.LineEdit2.setObjectName("LineEdit2")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 280, 131, 91))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(85, 255, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.Cuenta_Parametros)
        

        self.setWindowTitle("Ingresar planta")
        self.label_3.setText( "Ingresar la frecuencia")
        self.label_2.setText("Ingresar el nombre del parametro")
        self.pushButton_2.setText("INGRESAR")

        



##### EDITAR PLANTAS :D#####
class Editar_Planta(QDialog):

    def openWindow6(self):
        self.Actualizar_Planta.exec_()###
    
    def openWindow5(self):
        self.Eliminar_Planta.exec_()###


        
    def __init__(self):

        self.Eliminar_Planta = Eliminar_Planta()
        self.Actualizar_Planta = Actualizar_Planta()

        QDialog.__init__(self)
        self.setObjectName("self")
        self.resize(320, 131)
        self.pushButton_5 = QtWidgets.QPushButton(self)
        self.pushButton_5.setGeometry(QtCore.QRect(50, 20, 211, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.pushButton_5.setObjectName("pushButton_5")

        self.pushButton_5.clicked.connect(self.openWindow5)

        self.pushButton_6 = QtWidgets.QPushButton(self)
        self.pushButton_6.setGeometry(QtCore.QRect(50, 70, 211, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color: rgb(170, 170, 135);")
        self.pushButton_6.setObjectName("pushButton_6")

        self.pushButton_6.clicked.connect(self.openWindow6)

        QtCore.QMetaObject.connectSlotsByName(self)

        self.setWindowTitle("Editar Planta")
        self.pushButton_5.setText("ELIMINAR PLANTA")
        self.pushButton_6.setText("ACTUALIZAR PLANTA")

class Eliminar_Planta(QDialog): ########
    global hashmap
    def Confirmation(self):        
        
        plant_Name = self.textEdit.toPlainText()
        planta1 = Plant(plant_Name)
        hashmap.Remove(planta1)
        self.textEdit.clear()
        print(hashmap.Hashtable)
        self.msg = QtWidgets.QMessageBox()
        self.msg.setInformativeText("Planta eliminada")
        self.msg.show()
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setWindowTitle("Notificacion")
        
        
    def __init__(self):
        QDialog.__init__(self)
        self.setObjectName("eliminar")
        self.resize(391, 204)
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(40, 20, 311, 71))
        font = QtGui.QFont()
        font.setFamily("Goudy Old Style")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(self)
        self.textEdit.setGeometry(QtCore.QRect(40, 100, 171, 91))
        self.textEdit.setObjectName("textEdit")
        self.botonEliminar = QtWidgets.QPushButton(self)
        self.botonEliminar.setGeometry(QtCore.QRect(240, 100, 131, 91))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.botonEliminar.setFont(font)
        self.botonEliminar.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.botonEliminar.setObjectName("botonEliminar")
        self.botonEliminar.clicked.connect(self.Confirmation)

        QtCore.QMetaObject.connectSlotsByName(self)

        
        self.setWindowTitle("Dialog")
        self.label_2.setText("<html><head/><body><p align=\"center\">SELECCIONE LA PLANTA</p><p align=\"center\">QUE DESEE ELIMINAR</p></body></html>")
        self.botonEliminar.setText("ELIMINAR")
    
class Actualizar_Planta(QDialog):
    global hashmap

    def actualizacion(self):
        print(self.lineEdit.text())
        print(self.lineEdit_2.text())
        a = hashmap.Find(self.lineEdit.text())
        print(a)
        hashmap.Remove(a)
        planta1 = Plant(self.lineEdit_2.text())
        hashmap.Insert(planta1)
        print(hashmap.Hashtable)

    def __init__(self):
        QDialog.__init__(self)
        self.setObjectName("Dialog")
        self.resize(457, 329)
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(20, 90, 281, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 230, 281, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(310, 150, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Goudy Old Style")
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(10, 30, 361, 41))
        font = QtGui.QFont()
        font.setFamily("Goudy Old Style")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(16, 180, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Goudy Old Style")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.setWindowTitle("Dialog")
        self.pushButton.setText("Actualizar")
        self.label.setText("Inserte el nombre de la planta a modificar")
        self.label_2.setText("Inserte nuevo nombre de la planta")
        self.setWindowTitle("Dialog")
        self.pushButton.setText("ACTUALIZAR")
        self.pushButton.clicked.connect(self.actualizacion)
        self.label_2.setText("<html><head/><body><p align=\"center\">ESCRIBA LA PLANTA</p><p align=\"center\">QUE DESEE ACTUALIZAR</p></body></html>")




#Notificaciones
class Notificacion(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setObjectName("Dialog")
        self.resize(400, 300)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(40, 100, 271, 171))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")

        QtCore.QMetaObject.connectSlotsByName(self)

        self.setWindowTitle("Notificaciones")
        self.label.setText("NOTIFICACIONES")

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



