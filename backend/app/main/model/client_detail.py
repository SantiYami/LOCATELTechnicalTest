from .. import db
from werkzeug.security import generate_password_hash, check_password_hash

class ClientDetail(db.Model):
    __tablename__ = 'client_detail'
    __table_args__ = {'comment': 'Tabla que almacena información adicional específica de los clientes'}

    id_client_detail = db.Column(db.Integer, primary_key=True, autoincrement=True, info={'comment': 'Identificador único de los detalles del cliente'})
    user_id = db.Column(db.Integer, db.ForeignKey('user.id_user'), nullable=False, info={'comment': 'Identificador del usuario que es un cliente'})
    name = db.Column(db.String(100), nullable=False, info={'comment': 'Nombre completo del cliente'})
    address = db.Column(db.String(200), nullable=True, info={'comment': 'Dirección del cliente'})
    phone = db.Column(db.String(20), nullable=True, info={'comment': 'Número de teléfono del cliente'})

    # Relación con la tabla de usuarios
    user = db.relationship('User', backref=db.backref('client_details', uselist=False))