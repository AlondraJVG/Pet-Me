from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Producto, Base

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

if __name__ == "__main__":
    main()
