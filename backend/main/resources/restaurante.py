from flask_restful import Resource
from flask import request
from main import db
from main.models.restaurante import Restaurantes

class RestauranteResources(Resource):
    def get(self):
        restaurantes = Restaurantes.query.all()
        return [{
            "id": r.id,
            "nombre": r.nombre,
            "horario": r.horario,
            "ubicacion": r.ubicacion,
            "tipo_comida_id": r.tipo_comida_id
        } for r in restaurantes]

    def post(self):
        data = request.get_json()
        restaurante = Restaurantes(
            nombre=data["nombre"],
            horario=data["horario"],
            ubicacion=data["ubicacion"],
            tipo_comida_id=data["tipo_comida_id"]
        )
        db.session.add(restaurante)
        db.session.commit()
        return {
            "id": restaurante.id,
            "nombre": restaurante.nombre,
            "horario": restaurante.horario,
            "ubicacion": restaurante.ubicacion,
            "tipo_comida_id": restaurante.tipo_comida_id
        }, 201
