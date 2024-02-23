from flask import Flask, request, jsonify

# Simulación de una base de datos de usuarios
usuarios = {
    "usuario1": "contraseña1",
    "usuario2": "contraseña2",
    # Agrega más usuarios según sea necesario
}

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    # Obtener el nombre de usuario y la contraseña del cuerpo de la solicitud
    username = data.get('usuario')
    password = data.get('contraseña')

    # Verificar si el nombre de usuario existe y si la contraseña es correcta
    if username in usuarios and usuarios[username] == password:
        return jsonify({'mensaje': 'Inicio de sesión exitoso'}), 200
    else:
        return jsonify({'mensaje': 'Nombre de usuario o contraseña incorrectos'}), 401

if __name__ == '__main__':
    app.run(debug=True)
