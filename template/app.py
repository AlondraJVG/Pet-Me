from flask import Flask, render_template, redirect, url_for

# Creamos una instancia de la aplicación Flask
app = Flask(__name__)

# Definimos la ruta para la página de inicio
@app.route('/')
def login():
    return render_template('login.html')

# Definimos la ruta para la segunda página
@app.route('/pagina2')
def pagina2():
    return render_template('pagina2.html')

# Definimos una ruta para redireccionar al índice
@app.route('/regresar_al_index')
def regresar_al_index():
    return redirect(url_for('index'))

# Si este archivo es ejecutado directamente, arrancamos el servidor
if __name__ == '__main__':
    app.run(debug=True)
