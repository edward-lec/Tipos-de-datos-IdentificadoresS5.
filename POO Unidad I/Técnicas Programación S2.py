"""
Ejemplo de Programación Orientada a Objetos

Realizado Por: Leiber Correa
Descripción:
    Este programa muestra el uso de las principales técnicas de POO:
    - Abstracción
    - Encapsulación
    - Herencia
    - Polimorfismo

    Se utiliza como contexto una pequeña jerarquía de vehículos.
"""

from abc import ABC, abstractmethod


# CLASE BASE ABSTRACTA o ABSTRACCIÓN

# La clase Vehiculo representa la estructura general que cualquier
# vehículo debería tener. No se crea directamente, sino que sirve
# como guía para las clases hijas.


class Vehiculo(ABC):

    def __init__(self, marca: str, modelo: str):
        # Atributos protegidos (encapsulación simple)
        self._marca = marca
        self._modelo = modelo

    # Métodos GET y SET → Encapsulación correcta
    def get_modelo(self) -> str:
        """Devuelve el modelo del vehículo."""
        return self._modelo

    def set_modelo(self, nuevo_modelo: str) -> None:
        """
        Permite modificar el modelo.
        Incluye una validación mínima para evitar valores inválidos.
        """
        if isinstance(nuevo_modelo, str) and nuevo_modelo.strip():
            self._modelo = nuevo_modelo

    @abstractmethod
    def descripcion(self) -> str:
        """
        Método abstracto. Las clases hijas deben implementar este método.
        Refuerza la abstracción obligando a cada vehículo a describirse.
        """
        pass



# CLASE HIJA: AUTO o HERENCIA + POLIMORFISMO

# Hereda de Vehiculo y agrega atributos específicos.
# Implementa su propia versión del método "descripcion".


class Auto(Vehiculo):

    def __init__(self, marca: str, modelo: str, puertas: int):
        super().__init__(marca, modelo)
        self._puertas = puertas

    def descripcion(self) -> str:
        """Devuelve una descripción específica para un auto."""
        return f"Auto {self._marca} {self._modelo} con {self._puertas} puertas."



# CLASE HIJA: MOTO o HERENCIA + POLIMORFISMO

# Igual que Auto, pero con su propio atributo distintivo.


class Moto(Vehiculo):

    def __init__(self, marca: str, modelo: str, tipo_motor: str):
        super().__init__(marca, modelo)
        self._tipo_motor = tipo_motor

    def descripcion(self) -> str:
        """Devuelve una descripción adaptada a una motocicleta."""
        return f"Moto {self._marca} {self._modelo}, motor: {self._tipo_motor}."



# FUNCIÓN PRINCIPAL o PRUEBA DEL CÓDIGO

# Aquí se comprueba el polimorfismo: ambos objetos comparten el mismo
# método, pero cada uno devuelve un resultado distinto.
# También se muestra el uso de la encapsulación.


def main():
    auto1 = Auto("Toyota", "Corolla", 4)
    moto1 = Moto("Yamaha", "MT-03", "321cc")

    vehiculos = [auto1, moto1]

    print("=== Descripciones de los vehículos ===")
    for v in vehiculos:
        # Polimorfismo en acción
        print(v.descripcion())

    print("\n=== Probando encapsulación (setter/getter) ===")
    moto1.set_modelo("MT-03 Edición 2025")
    print("Modelo actualizado:", moto1.get_modelo())


# El típico punto de entrada del programa
if __name__ == "__main__":
    main()
