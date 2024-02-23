username = input('Escribe tu username =>')
valid_users = ['jose123','andrea456','maria789']

if username in valid_users:
  print('usuario valido, puedes continuar')
  password = input('ingresa tu contrasena =>')
  valid_password = ('PYnative@#2023')
  if password == valid_password:
    print('Bienvenido a tu portal de trabajo!')
else:
  print('usuario invalido, contacte a su administrador para solicitar ingreso')