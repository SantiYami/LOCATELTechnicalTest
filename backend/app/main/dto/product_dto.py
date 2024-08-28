from flask_restx import fields, Namespace

class ProductDto:
    api = Namespace('products', description='Operaciones relacionadas con productos')

    product_model = api.model('Product', {
        'code': fields.String(required=True, description='Código del producto'),
        'name': fields.String(required=True, description='Nombre del producto'),
        'sale_value': fields.Float(required=True, description='Valor de venta del producto'),
        'iva_handling': fields.Boolean(required=True, description='Indica si el producto maneja IVA'),
        'iva_percentage': fields.Float(description='Porcentaje de IVA si el producto maneja IVA')
    })
