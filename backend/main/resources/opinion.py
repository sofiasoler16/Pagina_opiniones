from flask_restful import Resource
from flask import request
from main import db
from main.models.opinion import Opiniones

class OpinionResources(Resource):
    def get(self):
        opiniones = Opiniones.query.all()
        return [{
            "id": o.id,
            "comentario": o.comentario,
            "valoracion": o.valoracion,
            "restaurante_id": o.restaurante_id,
            "usuario_id": o.usuario_id
        } for o in opiniones]

    def post(self):
        data = request.get_json()
        opinion = Opiniones(
            comentario=data["comentario"],
            valoracion=data["valoracion"],
            restaurante_id=data["restaurante_id"],
            usuario_id=data["usuario_id"]
        )
        db.session.add(opinion)
        db.session.commit()
        return {
            "id": opinion.id,
            "comentario": opinion.comentario,
            "valoracion": opinion.valoracion,
            "restaurante_id": opinion.restaurante_id,
            "usuario_id": opinion.usuario_id
        }, 201
