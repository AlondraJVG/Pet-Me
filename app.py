from flask import Flask, render_template, request
from flask_orator import Orator

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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    user = db.table("usuarios").where("user", username).where("password", password).get().first()

    if user is not None:
        return render_template('Adminitrador.py')
    else:
        return 'Nombre de usuario o contraseña incorrectos. Por favor, inténtelo de nuevo.'

if __name__ == '__main__':
    app.run(debug=True)