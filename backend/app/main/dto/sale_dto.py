from flask_restx import fields, Namespace

class SaleDto:
    api = Namespace('sales', description='Operaciones relacionadas con ventas')

    sale_header_model = api.model('SaleHeader', {
        'consecutive': fields.String(required=True, description='Número consecutivo de la venta'),
        'date': fields.DateTime(required=True, description='Fecha de la venta'),
        'client_id': fields.Integer(required=True, description='ID del cliente que realizó la compra'),
        'total_sale': fields.Float(required=True, description='Monto total de la venta')
    })

    sale_detail_model = api.model('SaleDetail', {
        'sale_id': fields.Integer(required=True, description='ID de la venta a la que pertenece el detalle'),
        'product_id': fields.Integer(required=True, description='ID del producto'),
        'product_value': fields.Float(required=True, description='Valor del producto en el detalle de la venta'),
        'calculated_iva': fields.Float(required=True, description='IVA calculado para el producto en el detalle')
    })