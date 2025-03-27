from .. import db

class Usuarios(db.Model):
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)
    nombre_usuario = db.Column(db.String(50), nullable=False)
    correo = db.Column(db.String(100), nullable=False, unique=True)
    contraseña = db.Column(db.String(100), nullable=False)


    opiniones = db.relationship("main.models.opinion.Opiniones", back_populates="usuario", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Usuarios: {self.nombre_usuario}>"