# ============================================================
# modelos/producto.py
# Clase que representa un producto disponible en el restaurante
# (comida, bebida, postre item del menú)
# ============================================================

class Producto:
    # Inicializa los atributos del producto
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    def mostrar_informacion(self):
        return f"Producto: {self.nombre} | Precio: ${self.precio} | Categoría: {self.categoria}"

    # Representación en texto del objeto producto
    def __str__(self):
        return f"{self.nombre} - ${self.precio} ({self.categoria})"