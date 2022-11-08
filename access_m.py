class User:
    def __init__(self) -> object:
        self.email = input('Introduzca su email: ')
        self.__password = input('Introduzca la contraseña: ')
        self.permissions = ('edit', 'create', 'update')
        self.username = None

    def setear_username(self):
        self.username = input('Introduzca el nombre  de usuario que desee: ')
        print(f'Nombre de usuario cambiado exitosamente a {self.username}')


print(User().__dict__)
