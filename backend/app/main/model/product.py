
from .. import db
from .supplier import Supplier

class Product(db.Model):
    __tablename__ = 'product'

    id_product = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price_unit = db.Column(db.Numeric, nullable=False)
    id_supplier = db.Column(db.ForeignKey('supplier.id_supplier'), nullable=False)

    supplier = db.relationship('Supplier', primaryjoin='Product.id_supplier == Supplier.id_supplier', backref='products')