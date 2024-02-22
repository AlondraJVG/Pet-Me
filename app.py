
from flask import flask

app=flask(__name__)

@app.route("/")
def prueba1():
    return "1"

if __name__=='__name__':
    app.run()
