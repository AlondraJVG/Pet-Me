from sqlalchemy import create_engine, Column, Integer, String, Text, DECIMAL, TIMESTAMP, Enum, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:///veterinaria_inventario.db', echo=True)

Base = declarative_base()

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

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

nuevo_producto = Producto(nombre="Alimento para gatos", tipo="Alimento", descripcion="Alimento balanceado para gatos adultos", precio=15.99, cantidad_stock=100)
session.add(nuevo_producto)
session.commit()

productos = session.query(Producto).all()
for producto in productos:
    print(f"ID: {producto.id}, Nombre: {producto.nombre}, Tipo: {producto.tipo}, Precio: {producto.precio}, Stock: {producto.cantidad_stock}")

session.close()
