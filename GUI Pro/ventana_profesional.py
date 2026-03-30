import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,  # Es como QWidget pero tiene su propia barra de menú, estatus, etc.
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class VentanaPrincipal(QMainWindow):  # Heredamos de QMainWindow
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi App Profesional")

        # Se crea un widget en el que se puedan poner layouts (Central Widget)
        self.contenedor_central = QWidget()
        self.setCentralWidget(
            self.contenedor_central
        )  # Aquí se establece un widget central

        # Ahora se crean los layouts dentro del Central WIdget
        self.layout_principal = QVBoxLayout()
        self.contenedor_central.setLayout(self.layout_principal)

        # Ahora se pueden añadir cosas al layout
        self.layout_principal.addWidget(QPushButton("Botón"))


app = QApplication(sys.argv)
ventana = VentanaPrincipal()
ventana.show()
sys.exit(app.exec())
