from flask_restful import Resource
from flask import request, abort
from main import db

from main.models.restaurante import Restaurantes
from main.models.tipo_comida import TipoComida

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

        tipo_comida = data.get('tipo_comida_id')
        if not db.session.query(TipoComida).get(tipo_comida):
            abort(404, description=f"No existe el tipo de comida con id {tipo_comida}")

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
    
    def delete(self, id):
        try:
            restaurante = Restaurantes.query.filter_by(id=id).first()
            db.session.delete(restaurante)
            db.session.commit()
            return {"message": "Restaurante {} eliminado".format(id)}, 200
        except Exception as e:
            db.session.rollback()
            abort(404, message=str(
                "404 Not Found: No se encuentra el restaurante de id" + id))
