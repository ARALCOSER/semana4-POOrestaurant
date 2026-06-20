# 📚 Restaurante App - Programación Orientada a Objetos en Python

## 📖 Descripción del Proyecto

Restaurante App es una aplicación desarrollada en Python utilizando el paradigma de **Programación Orientada a Objetos (POO)**.

El objetivo del proyecto es demostrar la creación e interacción de clases, objetos, atributos y métodos mediante un sistema básico de gestión de Restaurante. La aplicación permite registrar productos y clientes dentro de un restaurante y visualizar la información almacenada.

Este proyecto ha sido estructurado siguiendo una organización modular para facilitar el mantenimiento, la reutilización del código y la comprensión de los conceptos fundamentales de la POO.

---

## 🎯 Entidades mínimas sugeridas

El proyecto tiene las siguientes entidades:

- Producto: representa un plato, o producto disponible en el restaurante.
- Cliente: representa una persona que realiza o consume un pedido.
- Restaurante: administra los productos y clientes registrados en el sistema.

---

## ✅ Estructura del Proyecto

```text
restaurante_app/
│
├── modelos/
│   ├── cliente.py
│   └── producto.py
│
├── servicios/
│   └── restaurante.py
│
└── main.py
```

### Descripción de Carpetas

| Carpeta | Función |
|----------|----------|
| modulos | Contiene las clases que representan las entidades principales del sistema. |
| servicios | Contiene la lógica de gestión y administración de objetos. |
| main.py | Punto de entrada de la aplicación. |

---

## 📚 Clases Implementadas

### Producto

Representa un Producto dentro del sistema.

**Atributos:**

- nombre
- precio
- categoria

**Métodos:**

- mostrar_informacion
- __str__()

---

### Cliente

Representa un Cliente registrado en el Restaurante.

**Atributos:**

- nombre
- cedula

**Métodos:**

- mostrar_informacion
- __str__()

---

### Restaurante

Administra la colección de Producto y Clientes.

**Atributos:**

- Producto
- registro_clientes

**Métodos:**

- agregar_producto(self, producto)
- agregar_cliente(self, cliente)
- mostrar_cliente(self)
-  mostrar_producto(self)

---

## 🔄 Funcionamiento General

El programa realiza las siguientes acciones:

1. Inicialización y Creación de Objetos.
2. Carga y Registro de Datos (Procesamiento)
3. Generación del Reporte (Salida de Datos)

---

## 💻 Ejecución del Programa

Ubicarse en la carpeta principal del proyecto y ejecutar:

```bash
python main.py
```

---

## 🖥️ Salida Esperada

```text
PRODUCTOS:
Pizza - $10 (Comida rápida)
Ensalada Rusa - $7 (Saludable)
Sopa - $5 (Comida ligera)
Hamburguesa - $8 (Comida rápida)
Lomo Fino 700 gr - $16 (Plato fuerte)

CLIENTES:
Juan Salazar (0123456789)
María Ramos (0602964560)
Pedro López (0703857463)
```

---

## 🧩 Conceptos de Programación Orientada a Objetos Aplicados

### Clase

Una clase funciona como una plantilla para crear objetos.

Ejemplo:

```python
class Producto:
    pass
```

---

### Objeto

Un objeto es una instancia creada a partir de una clase.

Ejemplo:

```python
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
```

---

### Atributos

Son las características que describen a un objeto.

Ejemplo:

```python
class Producto:
    # Inicializa los atributos del producto
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
```

---

### Métodos

Son las acciones que puede realizar un objeto.

Ejemplo:

```python

    def mostrar_informacion(self):
        return f"Producto: {self.nombre} | Precio: ${self.precio} | Categoría: {self.categoria}"

    # Representación en texto del objeto producto
    def __str__(self):
        return f"{self.nombre} - ${self.precio} ({self.categoria})"

```

---

### Modularización

El proyecto se encuentra dividido en varios archivos para mejorar la organización y facilitar el mantenimiento del software.

Ventajas:

- Mayor claridad.
- Reutilización de código.
- Escalabilidad.
- Mantenimiento simplificado.
- Mejor trabajo colaborativo.

---

## 🚀 Posibles Mejoras Futuras

Este proyecto puede ampliarse incorporando funcionalidades como:

- Registro de pedidos.
- Cancelación o pago de cuenta.
- Búsqueda por Cédula.
- Eliminación de registros.

---

## 👨‍💻 Tecnologías Utilizadas

- Python 3.14.x
- Programación Orientada a Objetos (POO)

---

## 📑 Autor

Angel Ramiro Alcoser Allaica

---

## 📄 Licencia

Este proyecto puede utilizarse con fines académicos y de aprendizaje.

---

## ✅ Reflexión

Modularizar el software y separar responsabilidades no es solo una buena práctica, es una inversión en claridad y sostenibilidad. Cuando cada parte del sistema tiene una función bien definida, el código se vuelve más fácil de entender, mantener y escalar. Esto reduce errores, facilita el trabajo en equipo y permite que los cambios se hagan sin afectar todo el sistema. En esencia, un software bien modularizado refleja orden mental: divide lo complejo en partes simples para construir soluciones más robustas y estables.

