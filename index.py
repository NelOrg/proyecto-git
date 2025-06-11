# generar un codigo ramdom de prueba en python para modificar
# luego usando GIT para hacer pruebas de commit y push
import random
import string
def generate_random_code(length=10):
    """Genera un código aleatorio de letras y números."""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))    

if __name__ == "__main__":
    # Generar y mostrar un código aleatorio
    random_code = generate_random_code(10)
    print(f"Código aleatorio generado: {random_code}")
    
    # Aquí puedes agregar más lógica o funciones según sea necesario
    # Por ejemplo, podrías guardar el código en un archivo o base de datos
    # o realizar otras operaciones con él.
    # Este es un ejemplo simple para comenzar a trabajar con GIT
    # y hacer pruebas de commit y push.
    # Puedes modificar este código para adaptarlo a tus necesidades.

    # Recuerda que para usar GIT, debes inicializar un repositorio,
    # hacer commit de los cambios y luego hacer push a un repositorio remoto.

    # Ejemplo de uso de GIT:
    # 1. Inicializar un repositorio GIT:
    #    git init
    # 2. Agregar el archivo al repositorio:
    #    git add index.py
    # 3. Hacer commit de los cambios:

    #    git commit -m "Generar código aleatorio"
    # 4. Hacer push a un repositorio remoto (asegúrate de tener configurado el remoto):

    #    git push origin main
    # Asegúrate de tener configurado tu repositorio remoto y de haber hecho
    # el primer commit antes de hacer push.
    # Puedes usar este código como base para realizar pruebas y aprender a usar GIT.
    # Recuerda que GIT es una herramienta poderosa para el control de versiones
    # y la colaboración en proyectos de desarrollo de software.