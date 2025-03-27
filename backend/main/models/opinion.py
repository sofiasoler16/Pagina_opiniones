from .. import db


class Opiniones(db.Model):
    __tablename__ = 'opiniones'

    id_opinion = db.Column(db.Integer, primary_key=True)
    comentario = db.Column(db.String(300), nullable=False)
    valoracion = db.Column(db.Integer, nullable=False)
    restaurante_id = db.Column(db.Integer, db.ForeignKey("restaurantes.id"), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"), nullable=False)

    restaurante = db.relationship("main.models.restaurante.Restaurantes", back_populates="opiniones")
    usuario = db.relationship("main.models.usuario.Usuarios", back_populates="opiniones")


    def __repr__(self):
        return f"<Opinion: {self.valoracion} - {self.comentario}>"
    
    # def to_json(self):
    #     return {
    #         'id': self.id,
    #         'comentario': self.comentario,
    #         'valoracion': self.valoracion,
    #         'prestamo_id': self.prestamo_id
    #     }
    # @staticmethod
    # def from_json(opinion_json):
    #     try:
    #         valoracion = int(opinion_json.get('valoracion'))  # Convertir a entero si es string
    #     except (ValueError, TypeError):
    #         raise ValueError('La valoración debe ser un número entero entre 1 y 5.')

    #     if not (1 <= valoracion <= 5):
    #         raise ValueError('La valoración debe estar entre 1 y 5.')

    #     return Opiniones(
    #         comentario=opinion_json.get('comentario'),
    #         valoracion=valoracion,  # Usar el valor convertido
    #         prestamo_id=opinion_json.get('prestamo_id')
    #     )
