from flask import Flask, render_template, request, redirect, url_for
from flask_orator import Orator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Producto, Base

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
    user = db.table("usuarios").where("user", username).where("password", password).first()

    if user is not None:
        return redirect(url_for('inventario'))  # Redirige al administrador al inventario
    else:
        return 'Nombre de usuario o contraseña incorrectos. Por favor, inténtelo de nuevo.'

@app.route('/inventario')
def inventario():
    main()  # Realiza operaciones en la base de datos
    return '¡Bienvenido al inventario!'  # Muestra la página de inventario

def main():
    engine = create_engine('sqlite:///veterinaria_inventario.db', echo=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Agregar un nuevo producto
    nuevo_producto = Producto(nombre="Alimento para gatos", tipo="Alimento", descripcion="Alimento balanceado para gatos adultos", precio=15.99, cantidad_stock=100)
    session.add(nuevo_producto)
    session.commit()

    # Consultar todos los productos
    productos = session.query(Producto).all()
    for producto in productos:
        print(f"ID: {producto.id}, Nombre: {producto.nombre}, Tipo: {producto.tipo}, Precio: {producto.precio}, Stock: {producto.cantidad_stock}")

    session.close()

if __name__ == '__main__':
    app.run(debug=True)
