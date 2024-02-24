from flask import Flask, render_template

from index import index
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pagina2')
def pagina2():
    return render_template('pagina2.html')

@app.route('/regresar_al_index')
def regresar_al_index():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
