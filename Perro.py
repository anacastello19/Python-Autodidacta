class Perro:
    #Contructor
    def __init__(self,nombre,tamaño, edad, color, raza):
        self.nombre=nombre
        self.tamaño=tamaño
        self.edad=edad
        self.color=color
        self.raza= raza
    #Metodos
    def ladrar(self):
        print(f' {self.nombre} esta ladrando')

    def hambre(self, hambre):
        if hambre:
            self.comer()
        else:
            print(f'{self.nombre} no tiene hambre')
    def comer(self):
        print(f'{self.nombre} esta comiendo')
    def jugar(self):
        print(f'{self.nombre} esta jugando')

    def cumple(self):
        self.edad += 1
        print(f"{self.nombre} ahora tiene {self.edad} años")

    #Getter/Setter
    def set_edad(self, edad):
        self.edad=edad
        print(f'{self.nombre} ahora tiene {self.edad}')
    def mostrar_detalles(self):
        print(f'Mi perro se llama {self.nombre}, su tamaño es {self.tamaño}, tiene {self.edad} años, tiene un color {self.color} y su raza es {self.raza}')

#Intanciar objeto
miPerro= Perro('Reyna', 'mediano', 16, 'rubio', 'convinacion de labrador y ovejero aleman.' )
miPerro.mostrar_detalles()
miPerro.ladrar()
miPerro.comer()
miPerro.jugar()
miPerro.cumple()
miPerro.hambre(True)
miPerro.set_edad(20)