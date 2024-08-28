from .. import db
from ..model.user import User

import logging
import traceback

def create_client(data):
    try:
        new_client = User(
            username=data['document_id'],
            email=data['email'],
            role='client',
            name=data['name'],
            address=data['address'],
            phone=data['phone']
        )
        new_client.set_password(data['password'])  # Assuming password is provided and needed
        db.session.add(new_client)
        db.session.commit()
        return {"message": "Client created successfully"}, 201
    except Exception as e:
        logging.error(e)
        logging.error(traceback.format_exc())
        response = {
            "message": "Error: " + str(e),
        }
        return response, 500
    finally:
        db.session.close()

def get_clients():
    try:
        clients = User.query.filter_by(role='client').all()
        clients_data = [
            {
                "id": client.id_user,
                "document_id": client.username,
                "name": client.name,
                "address": client.address,
                "phone": client.phone,
                "email": client.email
            } for client in clients
        ]
        return clients_data, 200
    except Exception as e:
        logging.error(e)
        logging.error(traceback.format_exc())
        response = {
            "message": "Error: " + str(e),
        }
        return response, 500
    finally:
        db.session.close()

def get_client(id):
    try:
        client = User.query.filter_by(id_user=id, role='client').first()
        if not client:
            return {"message": "No se encontró el cliente"}, 204
        client_data = {
            "id": client.id_user,
            "document_id": client.username,
            "name": client.name,
            "address": client.address,
            "phone": client.phone,
            "email": client.email
        }
        return client_data, 200
    except Exception as e:
        logging.error(e)
        logging.error(traceback.format_exc())
        response = {
            "message": "Error: " + str(e),
        }
        return response, 500
    finally:
        db.session.close()

def update_client(id, data):
    try:
        client = User.query.filter_by(id_user=id, role='client').first()
        if not client:
            return {"message": "No se encontró el cliente"}, 204
        client.name = data.get('name', client.name)
        client.address = data.get('address', client.address)
        client.phone = data.get('phone', client.phone)
        client.email = data.get('email', client.email)
        db.session.commit()
        return {"message": "Client updated successfully"}, 200
    except Exception as e:
        logging.error(e)
        logging.error(traceback.format_exc())
        response = {
            "message": "Error: " + str(e),
        }
        return response, 500
    finally:
        db.session.close()

def delete_client(id):
    try:
        client = User.query.filter_by(id_user=id, role='client').first()
        if not client:
            return {"message": "No se encontró el cliente"}, 204
        db.session.delete(client)
        db.session.commit()
        return {"message": "Client deleted successfully"}, 200
    except Exception as e:
        logging.error(e)
        logging.error(traceback.format_exc())
        response = {
            "message": "Error: " + str(e),
        }
        return response, 500
    finally:
        db.session.close()
