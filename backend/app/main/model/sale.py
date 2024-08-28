from .. import db
from datetime import datetime

class Sale(db.Model):
    __tablename__ = 'sale'
    __table_args__ = {'comment': 'Tabla que almacena la cabecera de las ventas'}

    id_sale = db.Column(db.Integer, primary_key=True, autoincrement=True, info={'comment': 'Identificador único de la venta'})
    consecutive = db.Column(db.String(50), nullable=False, unique=True, info={'comment': 'Número consecutivo de la venta'})
    date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False, info={'comment': 'Fecha de la venta'})
    user_id = db.Column(db.Integer, db.ForeignKey('user.id_user'), nullable=False, info={'comment': 'Identificador del usuario que realizó la compra'})
    total_sale = db.Column(db.String(30), nullable=False, info={'comment': 'Monto total de la venta'})

    # Definición de relación con la tabla User
    user = db.relationship('User', backref=db.backref('sales', lazy=True))
