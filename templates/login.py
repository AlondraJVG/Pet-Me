def login():
    # Pedir al usuario que ingrese su nombre de usuario y contraseña
    username = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")

    # Verificar si el nombre de usuario y la contraseña son correctos
    if username == "usuario" and password == "contraseña":
        print("¡Inicio de sesión exitoso!")
    else:
        print("Nombre de usuario o contraseña incorrectos. Por favor, inténtelo de nuevo.")

# Ejecutar la función de login
login()
