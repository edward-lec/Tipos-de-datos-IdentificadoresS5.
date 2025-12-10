# Programa: Promedio semanal del clima (POO con herencia y polimorfismo)
# Elaborado por: Leiber Correa

class ClimaBase:
    """Clase base que representa un conjunto de temperaturas."""

    def __init__(self):
        self._temperaturas = []  # atributo protegido (encapsulamiento)

    def ingresar_temperaturas(self):
        """Método genérico que puede ser sobrescrito."""
        raise NotImplementedError("Este método debe implementarse en la subclase.")

    def calcular_promedio(self):
        """Cálculo genérico del promedio (puede ser sobrescrito)."""
        if len(self._temperaturas) == 0:
            return 0
        return sum(self._temperaturas) / len(self._temperaturas)


class ClimaSemanal(ClimaBase):
    """Clase derivada que gestiona temperaturas de una semana."""

    def ingresar_temperaturas(self):
        print("Ingrese la temperatura de cada día de la semana:\n")
        for i in range(7):
            temp = float(input(f"Día {i + 1}: "))
            self._temperaturas.append(temp)

    # POLIMORFISMO: Sobrescritura del método calcular_promedio()
    def calcular_promedio(self):
        print("\nCalculando promedio semanal...")
        return super().calcular_promedio()

    def mostrar_promedio(self):
        promedio = self.calcular_promedio()
        print(f"\nEl promedio semanal de temperatura es: {promedio:.2f}°C")


# Bloque principal
if __name__ == "__main__":
    print("=== PROMEDIO SEMANAL DEL CLIMA (POO) ===\n")

    clima = ClimaSemanal()      # Objeto de la clase hija (herencia)
    clima.ingresar_temperaturas()
    clima.mostrar_promedio()
