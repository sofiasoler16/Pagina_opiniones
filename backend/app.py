from flask import Flask
from main import create_app, db
import os


app = create_app()

app.app_context().push()

@app.route("/ping")
def ping():
    return "Servidor funcionando"


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host="0.0.0.0", port=int(os.getenv('PORT')))
