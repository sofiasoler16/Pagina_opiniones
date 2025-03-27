from .. import db



class Platos(db.Model):
    __tablename__ = 'platos'

    id_plato = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Integer, nullable=False)
    restaurante_id = db.Column(db.Integer, db.ForeignKey("restaurantes.id"), nullable=False)

    restaurante = db.relationship("main.models.restaurante.Restaurantes", back_populates="platos")
    
    def __repr__(self):
        return f"<Plato: {self.nombre} - ${self.precio}>"

    # @staticmethod
    # def from_json(libro_json):
    #     nombre = libro_json.get('nombre')
    #     genero = libro_json.get('genero')
    #     imagen_url = libro_json.get('imagen_url')
    #     return Libros(
    #         nombre=nombre,
    #         genero=genero,
    #         imagen_url=imagen_url
    #     )

    # def to_json(self):
    #     libro_json = {
    #         'id': self.id,
    #         'nombre': self.nombre,
    #         'genero': self.genero,
    #         'imagen_url': self.imagen_url,
    #         'stock': self.stock.cantidad if self.stock else None

    #     }
    #     return libro_json
