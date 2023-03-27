'''
i.Longuitud entre 6 a 12 caracteres
ii. Debe contener al menos un numero
iii. Debe contener al menos dos mayusculas
iv. Debe contener al menos un caracter especial
v. No puede contener especio
'''
import re

def valida_contraseña(contraseña):
    if not (6<=len(contraseña.replace(' ',''))<=20):
    #if len(contraseña.trim())>=6 and len(contraseña.trim()<=20):
        return False

    return True
    any_number_regex='[0-9]'
    if not re.search(any_number_regex,contraseña):
        return False

    any_capital_letter='[A-Z]{2,}'
    if re.search(any_capital_letter,contraseña):
        print('hay mayus')

    return True

print(valida_contraseña('holacomova5'))
