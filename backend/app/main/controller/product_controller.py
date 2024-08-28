from flask_restx import Resource
from flask import request
from ..service.product_service import create_product, get_products, get_product, update_product, delete_product
from ..dto.product_dto import ProductDto

api = ProductDto.api
product_model = ProductDto.product_model

@api.route('/products')
class ProductsResource(Resource):
    
    def get(self):
        """
        Obtiene los detalles de los productos.
        """
        response, status = get_products()
        return response, status

@api.route('/product')
class ProductResource(Resource):
    @api.expect(product_model)
    def post(self):
        """
        Crea un nuevo producto.
        """
        data = request.json
        response, status = create_product(data)
        return response, status
    
    @api.param('code', 'Código del producto')
    def get(self):
        """
        Obtiene los detalles de un producto por su código.
        """
        code = request.args.get("code")
        response, status = get_product(code)
        return response, status

@api.route('/product/<string:code>')
class ProductDetailResource(Resource):
    @api.expect(product_model)
    def put(self, code):
        """
        Actualiza un producto existente por su código.
        """
        data = request.json
        response, status = update_product(code, data)
        return response, status

    def delete(self, code):
        """
        Elimina un producto existente por su código.
        """
        response, status = delete_product(code)
        return response, status
