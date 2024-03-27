from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy  # Aquí asumiendo que estás usando SQLAlchemy para interactuar con la base de datos

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///veterinaria_inventario.db'
db = SQLAlchemy(app)

# Definir el modelo de Producto
class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    tipo = db.Column(db.String(50))
    descripcion = db.Column(db.Text)
    precio = db.Column(db.DECIMAL(10, 2))
    cantidad_stock = db.Column(db.Integer)

# Ruta para agregar un nuevo producto
@app.route('/agregar_producto', methods=['POST'])
def agregar_producto():
    nombre = request.form['nombre']
    tipo = request.form['tipo']
    descripcion = request.form['descripcion']
    precio = request.form['precio']
    cantidad_stock = request.form['cantidad_stock']

    # Crear una nueva instancia de Producto y agregarla a la base de datos
    nuevo_producto = Producto(nombre=nombre, tipo=tipo, descripcion=descripcion, precio=precio, cantidad_stock=cantidad_stock)
    db.session.add(nuevo_producto)
    db.session.commit()

    # Redirigir a la página de administrador o a donde desees
    return redirect(url_for('administrador'))

if __name__ == '__main__':
    app.run(debug=True)
