from flask import Flask, render_template, redirect, url_for, request
from orator import DatabaseManager, Model

app = Flask(__name__)

# Configurar la conexión a la base de datos
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

# Inicializar el administrador de la base de datos
db = DatabaseManager(config)
Model.set_connection_resolver(db)

# Definir el modelo de Producto
class Producto(Model):
    __table__ = 'Productos'
    __timestamps__ = False  # Si no hay campos de timestamp en la tabla

# Ruta para agregar un nuevo producto
@app.route('/agregar_producto', methods=['POST'])
def agregar_producto():
    # Obtener los datos del formulario
    nombre = request.form['nombre']
    tipo = request.form['tipo']
    descripcion = request.form['descripcion']
    precio = request.form['precio']
    cantidad_stock = request.form['cantidad_stock']

    # Crear una nueva instancia de Producto y guardarla en la base de datos
    nuevo_producto = Producto.create(nombre=nombre, tipo=tipo, descripcion=descripcion, precio=precio, cantidad_stock=cantidad_stock)

    # Redirigir a la página de administrador o a donde desees
    return redirect(url_for('administrador'))

# Ruta para la página del administrador
@app.route('/administrador')
def administrador():
    # Obtener la lista de productos desde la base de datos
    productos = Producto.all()
    # Pasar la lista de productos a la plantilla HTML
    return render_template('administrador.html', productos=productos)

if __name__ == '__main__':
    app.run(debug=True)
