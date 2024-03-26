from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Producto, Base
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/administrador')
def administrador():
    # Obtener la lista de productos
    productos = obtener_lista_de_productos()  
    return render_template('inventario.html', productos=productos)

def obtener_lista_de_productos():
    engine = create_engine('sqlite:///veterinaria_inventario.db', echo=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Consultar todos los productos
    productos = session.query(Producto).all()
    session.close()
    
    return productos

if __name__ == "__main__":
    app.run(debug=True)
