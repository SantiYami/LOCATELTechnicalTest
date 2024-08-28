from flask_restx import Resource
from flask import request
from ..service.auth_service import authenticate_user
from ..dto.auth_dto import AuthDto

api = AuthDto.api
auth_model = AuthDto.auth_model

@api.route('/login')
class AuthResource(Resource):
    @api.expect(auth_model)
    def post(self):
        """
        Autentica al usuario y devuelve un token JWT.
        """
        data = request.json
        email = data.get('email')
        password = data.get('password')
        
        # Autentica al usuario y obtiene el token
        response, status = authenticate_user(email, password)
        
        return response, status
