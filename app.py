from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def login():
    return render_Pet&Me("login.html")

if __name__=='__name__':
   
    app.run()

