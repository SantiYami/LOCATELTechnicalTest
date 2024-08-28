from flask_restx import fields, Namespace

class UserDto:
    api = Namespace('clients', description='Operaciones relacionadas con clientes')

    client_model = api.model('Client', {
        'document_id': fields.String(required=True, description='Identificador del documento del cliente'),
        'name': fields.String(required=True, description='Nombre del cliente'),
        'address': fields.String(required=True, description='Dirección del cliente'),
        'phone': fields.String(required=True, description='Teléfono del cliente'),
        'email': fields.String(required=True, description='Correo electrónico del cliente'),
        'password': fields.String(required=True, description='Contraseña del cliente')
    })
