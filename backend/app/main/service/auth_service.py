from .. import db
from ..model.user import User
import jwt
from datetime import datetime, timezone, timedelta
import logging
import traceback

SECRET_KEY = "861e8a53a7ba05aeabca6cf39bbdd908"


def get_current_utc_time():
    return datetime.now(timezone.utc)


def authenticate_user(email, password):
    try:
        user = User.query.filter_by(email=email).first()
        if not user or not user.check_password(
            password
        ):  # Assuming you have a check_password method
            return {"message": "Invalid email or password"}, 401

        # Generar token
        expiration_time = get_current_utc_time() + timedelta(hours=1)
        token = jwt.encode(
            {"id_user": user.id_user, "exp": expiration_time},
            SECRET_KEY,
            algorithm="HS256",
        )

        return {"token": token}, 200
    except Exception as e:
        logging.error(e)
        logging.error(traceback.format_exc())
        response = {
            "message": "Error: " + str(e),
        }
        return response, 500
