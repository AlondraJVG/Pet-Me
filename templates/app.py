from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username == 'usuario' and password == 'contraseña':
        return '¡Inicio de sesión exitoso!'
    else:
        return 'Nombre de usuario o contraseña incorrectos. Por favor, inténtelo de nuevo.'

if __name__ == '__main__':
    app.run(debug=True)
