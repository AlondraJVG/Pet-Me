class Administrador:
    def __init__(self, id_admin, nombre, apellido_paterno, apellido_materno, numero, correo):
        self.id_admin = id_admin
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.numero = numero
        self.correo = correo

    def __str__(self):
        return f"ID: {self.id_admin}\nNombre: {self.nombre} {self.apellido_paterno} {self.apellido_materno}\nNúmero: {self.numero}\nCorreo: {self.correo}"

    def cambiar_numero(self, nuevo_numero):
        self.numero = nuevo_numero

    def cambiar_correo(self, nuevo_correo):
        self.correo = nuevo_correo

# Ejemplo de uso
admin = Administrador(1, "Juan", "Pérez", "González", "1234567890", "juan@example.com")
print(admin)

# Cambiar número de teléfono
admin.cambiar_numero("0987654321")
print(admin)

# Cambiar correo electrónico
admin.cambiar_correo("juan.perez@example.com")
print(admin)
