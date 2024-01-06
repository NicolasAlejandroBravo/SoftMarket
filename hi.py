import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QDesktopWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class VentanaFullScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Ventana Full Screen en Modo Ventana')

        # Obtener la geometría de la pantalla
        screen_geometry = QDesktopWidget().screenGeometry()
        self.setGeometry(screen_geometry)

        # Cargar la imagen
        imagen_fondo = QPixmap("fondo.jpg")  # Reemplaza con la ruta de tu imagen

        # Configurar el fondo de la ventana con la imagen
        paleta = self.palette()
        paleta.setBrush(self.backgroundRole(), imagen_fondo)
        self.setPalette(paleta)

        # Crear botones
        boton1 = QPushButton('VENTAS', self)
        boton1.setFixedSize(120, 60)

        boton2 = QPushButton('INGRESOS', self)
        boton2.setFixedSize(120, 60)

        boton3 = QPushButton('CLIENTES', self)
        boton3.setFixedSize(120, 60)

        boton4 = QPushButton('PROVEEDORES', self)
        boton4.setFixedSize(120, 60)

        boton5 = QPushButton('STOCK', self)
        boton5.setFixedSize(120, 60)

        boton6 = QPushButton('USUARIOS', self)
        boton6.setFixedSize(120, 60)

        boton7 = QPushButton("CERRAR", self)
        boton7.setFixedSize(70, 60)
        boton7.setStyleSheet("background-color: red; color: white;")
        boton7.clicked.connect(QApplication.instance().quit)  # Conectar clic del botón a cerrar la aplicación

        # Crear layout horizontal para los botones
        layout_botones = QHBoxLayout()
        layout_botones.addWidget(boton1)
        layout_botones.addWidget(boton2)
        layout_botones.addWidget(boton3)
        layout_botones.addWidget(boton4)
        layout_botones.addWidget(boton5)
        layout_botones.addWidget(boton6)
        layout_botones.addWidget(boton7)
        
        # Crear layout vertical para la ventana
        layout_vertical = QVBoxLayout(self)
        layout_vertical.addLayout(layout_botones)

def main():
    app = QApplication(sys.argv)
    ventana = VentanaFullScreen()
    ventana.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
