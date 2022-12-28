from flask import Flask

app = Flask(__name__)

@app.router("/")
def hello_word():
    return "pelicula de cine"
