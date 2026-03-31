import sys

from PySide6.QtWidgets import QApplication, QWidget


# 1. Definimos nuestra propia clase de ventana
class MiVentana(QWidget):
    def __init__(self):
        super().__init__()  # Esto activa las funciones internas de QWidget
        self.setWindowTitle("Mi Primera App")  # Ponemos el título aquí dentro
        self.resize(400, 300)  # Le damos un tamaño inicial (Ancho, Alto)


app = QApplication(sys.argv)

# 2. Creamos una instancia de NUESTRA clase
window = MiVentana()
window.show()

sys.exit(app.exec())
