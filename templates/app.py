from flask import Flask, render_template, request, redirect, url_for
from flask_orator import Orator
from werkzeug.security import check_password_hash

ORATOR_DATABASES = {
    'development': {
        'driver': 'mysql',
        'host': 'petClinical.mysql.pythonanywhere-services.com',
        'database': 'petClinical$default',
        'user': 'petClinical',
        'password': 'Alondra.77'
    }
}

app = Flask(__name__)
app.config['ORATOR_DATABASES'] = ORATOR_DATABASES
db = Orator(app)

class Usuario(db.Model):
    __table__ = 'usuarios'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    user = Usuario.where("user", username).first()

    if user and check_password_hash(user.password, password):
        return redirect(url_for('administrador'))
    else:
        return 'Nombre de usuario o contraseña incorrectos. Por favor, inténtelo de nuevo.', 401

@app.route('/administrador')
def administrador():
    return render_template('administrador.html')

if __name__ == '__main__':
    app.run(debug=True)
