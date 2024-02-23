
from flask import Flask, render_template

from config import config 
app=Flask(__name__)

@app.route("/")
def prueba1():
    return render_template("index.html")

if __name__=='__name__':
    app.config.from_object(config['development'])
    app.run()
