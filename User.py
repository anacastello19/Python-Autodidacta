class User:
    def __init__(self) -> object:
        self.email= input('Introduzca su email: ')
        self.__password= input ('Introduzca la contraseña: ')
        self.permissions=('edit','create','update')
        self.username= None

    def setear_username(self):
        self.username= input('Introduzca el nombre  de usuario que desee: ')
        print(f'Nombre de usuario cambiado exitosamente a {self.username}')

class UserPro(User):
    def __init__(self):
     super().__init__()
     self.permissions+=['delete','download']

    def pay_suscription(self,monto):
        print('Usted ha pagado exitosamente la suscripcion ')

class UserManager:
    def create_user(self,suscripcion):
        if suscripcion:
            user= UserPro()
        else:
            user= User()
        print(f'Se ha creado exitosamente su usuario. Sus permisos son: {self.create_user()}')

UserManager().create_user(False)
