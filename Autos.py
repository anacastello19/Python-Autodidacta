from typing import Self


class Auto:
    #Contructor
    def __init__(self, modelo, color, ruedas, motor, puertas):
        self.modelo = modelo
        self.color = color
        self.ruedas = ruedas    
        self.motor = motor  
        self.puertas = puertas
        
    
    #Metodos
    def moverse(self):
        print(f'El {self.modelo} se mueve a una velocidad de 20km/h')

    def encender(self):
        print(f'El auto del modelo {self.modelo} se enciende')

    #getter/setter
    def set_color(self, color):
        self.color = color

    def mostrar_detalle(self):
        print(f'Tenemos un auto modelo: {self.modelo}, de color {self.color}, sus ruedas son {self.ruedas} pulgadas, con un motor de {self.motor} y tiene {self.puertas} puertas')
    
miAuto= Auto(2023, 'verde', 17, 3.1, 2)
miAuto.mostrar_detalle()
miAuto.encender()
miAuto.moverse()
miAuto.set_color('rojo')
miAuto.mostrar_detalle()