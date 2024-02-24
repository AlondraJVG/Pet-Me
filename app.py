from flask import Flask
from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def prueba1():
    return "1"
    return render_template("index.html")

if __name__=='__name__':
    app.run()