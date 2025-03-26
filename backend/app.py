from flask import Flask
from main import create_app
import os


app = create_app()

@app.route('/')
def home():
    return '¡Bienvenido a Opiniones de Comida!'

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv('PORT'))