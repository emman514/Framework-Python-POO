print("")
print("castruita soto emmanuel 3w 1176")
print("")
class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, value):
        if not isinstance(value, str):
            raise ValueError("El nombre debe ser una cadena de texto.")
        self._nombre = value
    @property
    def edad(self):
        return self._edad
    @edad.setter
    def edad(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("La edad debe ser un entero positivo.")
        self._edad = value
    @property
    def dni(self):
        return self._dni
    @dni.setter
    def dni(self, value):
        if not isinstance(value, str) or len(value) != 9:
            raise ValueError("El DNI debe ser una cadena de 9 caracteres.")
        self._dni = value
    def mostrar(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, DNI: {self.dni}"
class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        # Validar que titular sea una instancia de Persona
        if not isinstance(titular, Persona):
            raise ValueError("El titular debe ser una instancia de la clase Persona.")
        self.titular = titular
        self._cantidad = float(cantidad)
    @property
    def cantidad(self):
        return self._cantidad
    def ingresar(self, cantidad):
        # Solo permite ingresar cantidades positivas
        if cantidad > 0:
            self._cantidad += cantidad
    def retirar(self, cantidad):
        # Permite retirar cualquier cantidad, incluso dejando saldo negativo
        self._cantidad -= cantidad
    def mostrar(self):
        # Devuelve un mensaje con los datos de la cuenta
        return f"Titular: {self.titular.mostrar()}, Cantidad: {self.cantidad:.2f}"
try:
    persona1 = Persona("Juan Pérez", 30, "12345678A")
    cuenta = Cuenta(persona1, 500.0)
    print(cuenta.mostrar())  # Mostrar datos iniciales
    cuenta.ingresar(200)     # Ingresar 200
    cuenta.retirar(100)      # Retirar 100
    print(cuenta.mostrar())  # Mostrar datos actualizados
except Exception as e:
    print(f"Error: {e}")