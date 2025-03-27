from flask_restful import Resource
from flask import request
from main import db
from main.models.usuario import Usuarios

class UsuarioResources(Resource):
    def get(self):
        usuarios = Usuarios.query.all()
        return [{
            "id": u.id,
            "nombre_usuario": u.nombre_usuario,
            "correo": u.correo
        } for u in usuarios]

    def post(self):
        data = request.get_json()
        usuario = Usuarios(
            nombre_usuario=data["nombre_usuario"],
            correo=data["correo"],
            contraseña=data["contraseña"]
        )
        db.session.add(usuario)
        db.session.commit()
        return {
            "id": usuario.id,
            "nombre_usuario": usuario.nombre_usuario,
            "correo": usuario.correo
        }, 201
