from flask import Flask, render_template, request, jsonify
from orator import Model, DatabaseManager

app = Flask(__name__)

ORATOR_DATABASES = {
    'mysql': {
        'driver': 'mysql',
        'host': 'petClinical.mysql.pythonanywhere-services.com',
        'database': 'petClinical$default',
        'user': 'petClinical',
        'password': 'Alondra.77'
    }
}

db = DatabaseManager(ORATOR_DATABASES)
Model.set_connection_resolver(db)

class Producto(Model):
    __table__ = 'Productos'
    __timestamps__ = False

@app.route('/agregar_producto', methods=['POST'])
def agregar_producto():

    nombre = request.form['nombre']
    tipo = request.form['tipo']
    descripcion = request.form['descripcion']
    precio = request.form['precio']
    cantidad_stock = request.form['cantidad_stock']

    nuevo_producto = Producto.create(nombre=nombre, tipo=tipo, descripcion=descripcion, precio=precio, cantidad_stock=cantidad_stock)

    productos = Producto.all()
    productos_json = [{'id': producto.id, 'nombre': producto.nombre, 'tipo': producto.tipo,
                       'descripcion': producto.descripcion, 'precio': producto.precio,
                       'cantidad_stock': producto.cantidad_stock} for producto in productos]

    return jsonify(productos=productos_json)

@app.route('/')
def index():
    productos = Producto.all()
    return render_template('index.html', productos=productos)

if __name__ == '__main__':
    app.run(debug=True)
