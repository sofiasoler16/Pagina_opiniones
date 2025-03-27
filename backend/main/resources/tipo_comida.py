from flask_restful import Resource
from flask import request
from main import db

from main.models.tipo_comida import TipoComida

class TipoComidaResources(Resource):
    def get(self):
        tipos = TipoComida.query.all()
        return [{"id": t.id, "nombre": t.nombre} for t in tipos]

    def post(self):
        data = request.get_json()
        tipo = TipoComida(nombre=data["nombre"])
        db.session.add(tipo)
        db.session.commit()
        return {"id": tipo.id, "nombre": tipo.nombre}, 201
