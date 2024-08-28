from .. import db
from datetime import datetime, timedelta

class Session(db.Model):
    __tablename__ = 'session'
    __table_args__ = {'comment': 'Tabla que almacena las sesiones activas'}

    id_session = db.Column(db.Integer, primary_key=True, autoincrement=True, info={'comment': 'Identificador único de la sesión'})
    user_id = db.Column(db.Integer, db.ForeignKey('user.id_user'), nullable=False, info={'comment': 'Identificador del usuario al que pertenece la sesión'})
    token = db.Column(db.String(500), nullable=False, unique=True, info={'comment': 'Token de autenticación de la sesión'})
    expiration_date = db.Column(db.DateTime, nullable=False, default=lambda: datetime.utcnow() + timedelta(hours=1), info={'comment': 'Fecha de expiración de la sesión'})

    # Relación con la tabla de usuarios
    user = db.relationship('User', backref=db.backref('sessions', lazy=True))
