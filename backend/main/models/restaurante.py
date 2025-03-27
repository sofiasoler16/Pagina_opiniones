from .. import db



class Restaurantes(db.Model):
    __tablename__ = 'restaurantes'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    horario = db.Column(db.String(100), nullable=False)
    ubicacion = db.Column(db.String(100), nullable=False)
    tipo_comida_id = db.Column(db.Integer, db.ForeignKey("tipo_comida.id"), nullable=False)


    opiniones = db.relationship("main.models.opinion.Opiniones", back_populates="restaurante", cascade="all, delete-orphan")
    platos = db.relationship("main.models.plato.Platos", back_populates="restaurante", cascade="all, delete-orphan")
    tipo_comida = db.relationship("main.models.tipo_comida.TipoComida", back_populates="restaurantes")
    
    def __repr__(self):
        return ('<Restaurantes: %r >' % (self.nombre))
