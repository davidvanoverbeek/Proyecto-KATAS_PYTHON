# Ejercicio 34:

class Arbol:
    def __init__(self):
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        self.tronco += 1

    def nueva_rama(self):
        self.ramas.append(1)

    def crecer_ramas(self):
        self.ramas = [r + 1 for r in self.ramas]

    def quitar_rama(self, posicion):
        if 0 <= posicion < len(self.ramas):
            self.ramas.pop(posicion)

    def info_arbol(self):
        return {
            "tronco": self.tronco,
            "num_ramas": len(self.ramas),
            "longitudes_ramas": self.ramas
        }

if __name__ == "__main__":
    arbol = Arbol()
    arbol.crecer_tronco()
    arbol.nueva_rama()
    arbol.crecer_ramas()
    arbol.nueva_rama()
    arbol.nueva_rama()
    arbol.quitar_rama(2)
    print(arbol.info_arbol())
