# Definición de la clase base
class Animal:
    def _init_(self, nombre, edad):
        self.__nombre = nombre  # Atributo encapsulado
        self.edad = edad

    def hacer_sonido(self):
        pass  # Método que será sobrescrito por las clases derivadas

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

# Definición de la clase derivada
class Perro(Animal):
    def _init_(self, nombre, edad, raza):
        super()._init_(nombre, edad)
        self.raza = raza

    def hacer_sonido(self):
        return "Guau!"

# Otra clase derivada para demostrar polimorfismo
class Gato(Animal):
    def _init_(self, nombre, edad, color):
        super()._init_(nombre, edad)
        self.color = color

    def hacer_sonido(self):
        return "Miau!"

# Creación de instancias y demostración de funcionalidad
mi_perro = Perro("Firulais", 5, "Labrador")
mi_gato = Gato("Misu", 3, "Negro")

print(f"El perro {mi_perro.get_nombre()} de raza {mi_perro.raza} dice: {mi_perro.hacer_sonido()}")
print(f"El gato {mi_gato.get_nombre()} de color {mi_gato.color} dice: {mi_gato.hacer_sonido()}")

# Ejemplo de encapsulación: Intento de acceso directo al atributo encapsulado
try:
    print(mi_perro.__nombre)
except AttributeError as e:
    print(e)

# Uso de métodos getters y setters para acceder al atributo encapsulado
mi_perro.set_nombre("Max")
print(f"El nuevo nombre del perro es: {mi_perro.get_nombre()}")
