from flask import Flask, render_template, request
from flask_orator import Orator

app = Flask(__name__)

# Configuración de la base de datos
app.config['DATABASES'] = {
    'default': 'mysql',
    'connections': {
        'mysql': {
            'driver': 'mysql',
            'host': 'petClinical.mysql.pythonanywhere-services.com',
            'database': 'petClinical',
            'user': 'petClinical',
            'password': 'Alondra.77',
            'prefix': ''
        }
    }
}

db = Orator(app)

class Usuarios(db.Model):
    __table__ = 'usuarios'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    user = Usuarios.where("user", username).where("password", password).first()

    if user:
        return render_template('Administrador.py')
    else:
        return 'Nombre de usuario o contraseña incorrectos. Por favor, inténtelo de nuevo.'

if __name__ == '__main__':
    app.run(debug=True)
