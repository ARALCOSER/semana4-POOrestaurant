# ============================================================
# modelos/cliente.py
# Clase que representa a un cliente registrado en el restaurante
# ============================================================

class Cliente:
    def __init__(self, nombre, telefono):
        # Atributos básicos del cliente
        self.nombre = nombre
        self.telefono = telefono

    def mostrar_informacion(self):
        return f"Cliente: {self.nombre} | Teléfono: {self.telefono}"

    # Representación en texto del objeto cliente
    def __str__(self):
        return f"{self.nombre} ({self.telefono})"