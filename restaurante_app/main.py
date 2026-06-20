# ==============================================================================
# main.py
# Punto de arranque del sistema de gestión de restaurante.
# Aquí se crean los objetos y se ejecutan las operaciones 
# para demostrar el funcionamiento del sistema.
# ==============================================================================

# Importamos las clases de modelos y servicios

from servicios.restaurante import Restaurante
from modulos.producto import Producto
from modulos.cliente import Cliente

restaurante = Restaurante()

# Crear productos
producto1 = Producto("Pizza", 10, "Comida rápida")
producto2 = Producto("Ensalada Rusa", 7, "Saludable")
producto3 = Producto("Sopa", 5, "Comida ligera")
producto4 = Producto("Hamburguesa", 8, "Comida rápida")
producto5 = Producto("Lomo Fino 700 gr", 16, "Plato fuerte")

# Crear clientes
cliente1 = Cliente("Juan Salazar", "0123456789")
cliente2 = Cliente("María Ramos", "0602964560")
cliente3 = Cliente("Pedro López", "0703857463")

# Agregar a listas
restaurante.agregar_producto(producto1)
restaurante.agregar_producto(producto2)
restaurante.agregar_producto(producto3)
restaurante.agregar_producto(producto4)
restaurante.agregar_producto(producto5)
restaurante.agregar_cliente(cliente1)
restaurante.agregar_cliente(cliente2)
restaurante.agregar_cliente(cliente3)

# Mostrar
print("=== RESTAURANTE VACA & VACO ===\n")
print("PRODUCTOS:")
restaurante.mostrar_productos()

print("\nCLIENTES:")
restaurante.mostrar_clientes()

print("\n")