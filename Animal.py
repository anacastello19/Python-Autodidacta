class Animal:
    def __init__(self):
        self.edad= None
        self.especie= None
        self.pelaje=None

    def comer(self):
        print('El animal esta comiendo')

    def reproduccion(self):
        print('El animal se esta reproduciendo')

class Perro(Animal):
    def __init__(self):
        super().__init__()
        self.raza=None
        self.nombre= None

    def ladrar(self):
        print(f'El {self.nombre} esta ladrando')

    def jugar(self):
        print(f'El {self.nombre} esta jugando')

miPerro= Perro()
print(miPerro.edad)