from flask_restx import Resource
from flask import request
from ..service.sale_service import create_sale, get_sale, get_sales, get_sales_by_date
from ..dto.sale_dto import SaleDto

api = SaleDto.api
sale_header_model = SaleDto.sale_header_model

@api.route('/sale')
class SaleResource(Resource):
    @api.expect(sale_header_model)
    def post(self):
        """
        Crea una nueva venta.
        """
        data = request.json
        response, status = create_sale(data)
        return response, status
    
    @api.param('id', 'ID de la venta')
    def get(self):
        """
        Obtiene los detalles de una venta por su ID.
        """
        sale_id = request.args.get("id")
        response, status = get_sale(sale_id)
        return response, status

@api.route('/sales')
class SalesResource(Resource):
    def get(self):
        """
        Obtiene un listado de ventas realizadas.
        """
        
        response, status = get_sales()
        return response, status

@api.route('/sales/date')
class SalesByDateResource(Resource):
    @api.param('start_date', 'Fecha de inicio del rango (formato: YYYY-MM-DD)')
    @api.param('end_date', 'Fecha de fin del rango (formato: YYYY-MM-DD)')
    def get(self):
        """
        Obtiene un listado de ventas realizadas en un rango de fechas.
        """
        start_date = request.args.get("start_date")
        end_date = request.args.get("end_date")
        
        if not start_date or not end_date:
            return {"message": "Los parámetros 'start_date' y 'end_date' son requeridos."}, 400
        
        response, status = get_sales_by_date(start_date, end_date)
        return response, status
