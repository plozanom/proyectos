class Inventario:
    item_totales = 0

    def __init__(self, nombre_producto, precio, stock):
        self.nombre_producto = nombre_producto
        self.precio = precio
        self.stock = stock
        Inventario.item_totales += stock

    def detalle_producto(self):
        return f"Nombre del Producto: {self.nombre_producto}\nPrecio: {self.precio}\nCantidad: {self.stock}"

    def vender_producto(self, cantidad):
        if cantidad >= self.stock:
            self.stock -= cantidad
            Inventario.item_totales -= cantidad
            return f"Se vendieron {cantidad} {self.nombre_producto}"
        else:
            return "No hay suficiente stock"

    @classmethod
    def consulta_total_items(cls):
        return f"Numero total de Items: {cls.item_totales}"
