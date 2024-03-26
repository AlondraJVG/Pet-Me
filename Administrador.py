from flask import Flask, render_template
from sqlalchemy import create_engine, Column, Integer, String, Text, DECIMAL, TIMESTAMP, Enum, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)

# Definir la URL de la base de datos
DATABASE_URL = 'sqlite:///veterinaria_inventario.db'

# Crear el motor de la base de datos
engine = create_engine(DATABASE_URL, echo=True)

# Crear una instancia base para declarar las clases de las tablas
Base = declarative_base()

# Definir las clases para mapear a las tablas en la base de datos
class Producto(Base):
    __tablename__ = 'Productos'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    tipo = Column(String(50))
    descripcion = Column(Text)
    precio = Column(DECIMAL(10, 2))
    cantidad_stock = Column(Integer)

class Proveedor(Base):
    __tablename__ = 'Proveedores'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    direccion = Column(String(255))
    telefono = Column(String(20))

class TransaccionInventario(Base):
    __tablename__ = 'Transacciones_Inventario'
    id = Column(Integer, primary_key=True)
    producto_id = Column(Integer, ForeignKey('Productos.id'))
    tipo_transaccion = Column(Enum('Entrada', 'Salida'))
    cantidad = Column(Integer)
    fecha = Column(TIMESTAMP)
    proveedor_id = Column(Integer, ForeignKey('Proveedores.id'))

    producto = relationship("Producto", back_populates="transacciones")
    proveedor = relationship("Proveedor")

Producto.transacciones = relationship("TransaccionInventario", back_populates="producto")

# Crear una sesión para interactuar con la base de datos
Session = sessionmaker(bind=engine)
session = Session()

@app.route('/administrador')
def administrador():
    # Obtener la lista de productos
    productos = session.query(Producto).all()
    return render_template('inventario.html', productos=productos)

if __name__ == "__main__":
    app.run(debug=True)
