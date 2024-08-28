from .. import db

class Product(db.Model):
    __tablename__ = 'product'
    __table_args__ = {'comment': 'Tabla que almacena los datos de los productos'}

    id_product = db.Column(db.Integer, primary_key=True, autoincrement=True, info={'comment': 'Identificador único del producto'})
    code = db.Column(db.String(30), nullable=False, unique=True, info={'comment': 'Código del producto'})
    name = db.Column(db.String(100), nullable=False, info={'comment': 'Nombre del producto'})
    sale_value = db.Column(db.String(30), nullable=False, info={'comment': 'Valor de venta del producto'})
    handles_iva = db.Column(db.Boolean, nullable=False, default=False, info={'comment': 'Indicador si el producto maneja IVA'})
    iva_percentage = db.Column(db.String(4), nullable=True, info={'comment': 'Porcentaje de IVA aplicable si maneja IVA'})
