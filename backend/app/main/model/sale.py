from .. import db
from datetime import datetime

class Sale(db.Model):
    __tablename__ = 'sale'
    __table_args__ = {'comment': 'Tabla que almacena la cabecera de las ventas'}

    id_sale = db.Column(db.Integer, primary_key=True, autoincrement=True, info={'comment': 'Identificador único de la venta'})
    consecutive = db.Column(db.String(50), nullable=False, unique=True, info={'comment': 'Número consecutivo de la venta'})
    date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False, info={'comment': 'Fecha de la venta'})
    client_id = db.Column(db.Integer, db.ForeignKey('client.id_client'), nullable=False, info={'comment': 'Identificador del cliente que realizó la compra'})
    total_sale = db.Column(db.Numeric(10, 2), nullable=False, info={'comment': 'Monto total de la venta'})

    # Definición de relación con la tabla Client
    client = db.relationship('Client', backref=db.backref('sales', lazy=True))
