#crea un validar de email en python de prueba
import re
def validar_email(email):
    # Expresión regular para validar el formato del email
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if re.match(patron, email):
        return True
    else:
        return False
# Pruebas de la función validar_email
if __name__ == "__main__":
    emails = [
        "mail@mail.com",
    ]
    for email in emails:
        if validar_email(email):
            print(f"{email} es un email válido.")
        else:
            print(f"{email} no es un email válido.")
# Puedes agregar más pruebas aquí
# o modificar los existentes para probar diferentes casos.
# Ejemplo de uso
# email = "
#
# if validar_email(email):
#     print(f"{email} es un email válido.")
# else:
#     print(f"{email} no es un email válido.")
# Puedes agregar más pruebas aquí
# o modificar los existentes para probar diferentes casos.  
# Ejemplo de uso
# email = "
# if validar_email(email):
#     print(f"{email} es un email válido.") 
#new change
# new change 2