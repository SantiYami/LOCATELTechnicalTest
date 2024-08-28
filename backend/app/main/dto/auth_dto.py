from flask_restx import fields, Namespace

class AuthDto:
    api = Namespace('auth', description='Operaciones relacionadas con autentificación')

    auth_model = api.model('Auth', {
        'email': fields.String(required=True, description='Email del usuario'),
        'password': fields.String(required=True, description='Contraseña del usuario')
    })
