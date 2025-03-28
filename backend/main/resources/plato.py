from flask_restful import Resource
from flask import request, abort

from main import db

from main.models.plato import Platos
from main.models.restaurante import Restaurantes

class PlatoResources(Resource):
    def get(self):
        platos = Platos.query.all()
        return [{"id": t.id,
                  "nombre": t.nombre,
                    "precio": t.precio,
                      "restaurante_id": t.restaurante_id} for t in platos]

    def post(self):
        data = request.get_json()

        restaurante = data.get('restaurante_id')
        if not db.session.query(Restaurantes).get(restaurante):
            abort(404, description=f"No existe el restaurante con id {restaurante}")



        plato = Platos(
            nombre=data["nombre"], 
            precio=data["precio"], 
            restaurante_id=data["restaurante_id"])
        db.session.add(plato)
        db.session.commit()
        return {"id": plato.id,
                 "nombre": plato.nombre,
                   "precio": plato.precio,
                     "restaurante_id": plato.restaurante_id}, 201
    
    def delete(self, id):
        try:
            plato = Platos.query.filter_by(id=id).first()
            db.session.delete(plato)
            db.session.commit()
            return {"message": "Plato {} eliminado".format(id)}, 200
        except Exception as e:
            db.session.rollback()
            abort(404, message=str(
                "404 Not Found: No se encuentra el plato de id" + id))
