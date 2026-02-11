class Producto:
    def __init__(self, nombre: str, precio: float) -> None:
        self.nombre = nombre
        self.precio = precio


class ProductoElectronico(Producto):
    def __init__(self, nombre: str, precio: float, garantia_meses: int) -> None:
        super().__init__(nombre, precio)
        self.garantia_meses = garantia_meses
