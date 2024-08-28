from .. import db
from ..model.user import User
from ..model.client_detail import ClientDetail
import logging
import traceback


def create_client(data):
    try:
        # Crear un nuevo usuario
        new_user = User(
            username=data["document_id"], email=data["email"], role="client"
        )
        new_user.set_password(
            data["password"]
        )  # Assuming password is provided and needed
        db.session.add(new_user)
        db.session.commit()

        # Crear detalles del cliente
        client_detail = ClientDetail(
            id_user=new_user.id_user,
            name=data["name"],
            address=data["address"],
            phone=data["phone"],
        )
        db.session.add(client_detail)
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
        clients = (
            db.session.query(User, ClientDetail)
            .join(ClientDetail, User.id_user == ClientDetail.id_user)
            .filter(User.role == "client")
            .all()
        )
        clients_data = [
            {
                "id": user.id_user,
                "document_id": user.username,
                "name": detail.name,
                "address": detail.address,
                "phone": detail.phone,
                "email": user.email,
            }
            for user, detail in clients
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
        client = (
            db.session.query(User, ClientDetail)
            .join(ClientDetail, User.id_user == ClientDetail.id_user)
            .filter(User.id_user == id, User.role == "client")
            .first()
        )
        if not client:
            return {"message": "No se encontró el cliente"}, 204
        user, detail = client
        client_data = {
            "id": user.id_user,
            "document_id": user.username,
            "name": detail.name,
            "address": detail.address,
            "phone": detail.phone,
            "email": user.email,
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
        client = (
            db.session.query(User, ClientDetail)
            .join(ClientDetail, User.id_user == ClientDetail.id_user)
            .filter(User.id_user == id, User.role == "client")
            .first()
        )
        if not client:
            return {"message": "No se encontró el cliente"}, 204
        user, detail = client
        detail.name = data.get("name", detail.name)
        detail.address = data.get("address", detail.address)
        detail.phone = data.get("phone", detail.phone)
        user.email = data.get("email", user.email)
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
        client = (
            db.session.query(User)
            .filter(User.id_user == id, User.role == "client")
            .first()
        )
        if not client:
            return {"message": "No se encontró el cliente"}, 204
        ClientDetail.query.filter_by(id_user=id).delete()
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
