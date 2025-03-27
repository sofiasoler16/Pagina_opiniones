from flask_restful import Resource
from flask import request
from main import db

from main.models.plato import Platos

class PlatoResources(Resource):
    def get(self):
        platos = Platos.query.all()
        return [{"id": t.id, "nombre": t.nombre, "precio": t.precio, "restaurante_id": t.restaurante_id} for t in platos]

    def post(self):
        data = request.get_json()
        plato = Platos(nombre=data["nombre"], 
                       precio=data["precio"], 
                       restaurante_id=data["restaurante_id"])
        db.session.add(plato)
        db.session.commit()
        return {"id": plato.id,
                 "nombre": plato.nombre,
                   "precio": plato.precio,
                     "restaurante_id": plato.restaurante_id}, 201
