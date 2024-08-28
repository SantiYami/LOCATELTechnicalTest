from flask_restx import Resource
from flask import request
from ..service.client_service import create_client, get_client, update_client, delete_client

from ..dto.user_dto import UserDto

api = UserDto.api
client_model = UserDto.client_model

@api.route('/clients')
class ClientResource(Resource):
    @api.expect(client_model)
    def post(self):
        """
        Crea un nuevo cliente.
        """
        data = request.json
        response, status = create_client(data)
        return response, status
    
    @api.param('id', 'ID del cliente')
    def get(self):
        """
        Obtiene los detalles de un cliente por su ID.
        """
        client_id = request.args.get("id")
        response, status = get_client(client_id)
        return response, status

@api.route('/clients/<int:id>')
class ClientDetailResource(Resource):
    @api.expect(client_model)
    def put(self, id):
        """
        Actualiza un cliente existente por su ID.
        """
        data = request.json
        response, status = update_client(id, data)
        return response, status

    def delete(self, id):
        """
        Elimina un cliente existente por su ID.
        """
        response, status = delete_client(id)
        return response, status