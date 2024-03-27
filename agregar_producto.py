from flask import Flask, render_template, request, redirect, url_for
from orator import DatabaseManager, Model

app = Flask(__name__)

config = {
    'mysql': {
        'driver': 'mysql',
        'host': 'petClinical.mysql.pythonanywhere-services.com',
        'database': 'petClinical$default',
        'user': 'petClinical',
        'password': 'Alondra.77',
        'prefix': ''
    }
}

db = DatabaseManager(config)
Model.set_connection_resolver(db)

# Definir el modelo de Producto
class Producto(Model):
    __table__ = 'Productos'
    __timestamps__ = False  # Si no hay campos de timestamp en la tabla

# Ruta para agregar un nuevo producto
@app.route('/agregar_producto', methods=['POST'])
def agregar_producto():
    nombre = request.form['nombre']
    tipo = request.form['tipo']
    descripcion = request.form['descripcion']
    precio = request.form['precio']
    cantidad_stock = request.form['cantidad_stock']

    # Crear una nueva instancia de Producto y guardarla en la base de datos
    nuevo_producto = Producto.create(nombre=nombre, tipo=tipo, descripcion=descripcion, precio=precio, cantidad_stock=cantidad_stock)

    # Redirigir a la página de administrador o a donde desees
    return redirect(url_for('administrador'))

if __name__ == '__main__':
    app.run(debug=True)
