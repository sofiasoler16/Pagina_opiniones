from .. import db

class TipoComida(db.Model):
    __tablename__ = "tipo_comida"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False, unique=True)

    restaurantes = db.relationship("main.models.restaurante.Restaurantes", back_populates="tipo_comida", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<TipoComida: {self.nombre}>"
