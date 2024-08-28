from flask_restx import Resource
from flask import request
from ..service.sale_service import create_sale_detail, get_sale_detail
from ..dto.sale_dto import SaleDto

api = SaleDto.api
sale_detail_model = SaleDto.sale_detail_model

@api.route('/sale_details')
class SaleDetailResource(Resource):
    @api.expect(sale_detail_model)
    def post(self):
        """
        Crea un nuevo detalle de venta.
        """
        data = request.json
        response, status = create_sale_detail(data)
        return response, status
    
    @api.param('sale_id', 'ID de la venta')
    def get(self):
        """
        Obtiene los detalles de una venta por el ID de la venta y el ID del producto.
        """
        sale_id = request.args.get("sale_id")
        response, status = get_sale_detail(sale_id)
        return response, status
