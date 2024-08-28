from .. import db

class SaleDetail(db.Model):
    __tablename__ = 'sale_detail'
    __table_args__ = {'comment': 'Tabla que almacena los detalles de las ventas'}

    id_sale_detail = db.Column(db.Integer, primary_key=True, autoincrement=True, info={'comment': 'Identificador único del detalle de venta'})
    sale_id = db.Column(db.Integer, db.ForeignKey('sale.id_sale'), nullable=False, info={'comment': 'Identificador de la venta a la que pertenece este detalle'})
    product_id = db.Column(db.Integer, db.ForeignKey('product.id_product'), nullable=False, info={'comment': 'Identificador del producto vendido'})
    product_value = db.Column(db.Numeric(10, 2), nullable=False, info={'comment': 'Precio de venta del producto en esta transacción'})
    iva_calculated = db.Column(db.Numeric(10, 2), nullable=True, info={'comment': 'Valor del IVA calculado para este producto'})

    # Definición de relaciones
    sale = db.relationship('Sale', backref=db.backref('sale_details', lazy=True))
    product = db.relationship('Product', backref=db.backref('sale_details', lazy=True))
