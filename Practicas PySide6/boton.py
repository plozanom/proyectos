import sys

from PySide6.QtWidgets import QApplication, QPushButton, QWidget


class MiVentana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi App con Botón")
        self.resize(300, 200)
        # Creamos el botón y le decimos que la ventana es su padre agregandole el argumento self
        self.boton = QPushButton("Click aquí!!!!", self)
        # Le damos una posición al botón, si no se hace, saldrá en la esquina superior izquierda
        self.boton.move(100, 80)
        # Dandole funcionalidad al botón pasandole como argumento la función saludar
        self.boton.clicked.connect(self.saludar)

    def saludar(self):
        print(
            "El botón está funcionando!!!"
        )  # Se comprueba en la terminal que el botón funciona
        self.setWindowTitle(
            "Botón Pulsado!!!!"
        )  # Se cambia el titulo de la ventana al pulsar el botón


app = QApplication(sys.argv)
ventana = MiVentana()
ventana.show()
sys.exit(app.exec())
