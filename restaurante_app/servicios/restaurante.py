# ============================================================
# servicios/restaurante.py
# Clase de servicio que gestiona las operaciones principales
# del sistema: registro de productos y clientes.
# ============================================================


class Restaurante:
    def __init__(self):
        self.productos = []   # Lista de productos
        self.clientes = []   # Lista de clientes

    # ----------- PRODUCTOS -----------
    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        for producto in self.productos:
            print(producto)

    # ----------- CLIENTES -----------
    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def mostrar_clientes(self):
        for cliente in self.clientes:
            print(cliente)

