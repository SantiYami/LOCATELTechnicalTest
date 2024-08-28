from .. import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'user'
    __table_args__ = {'comment': 'Tabla que almacena los datos básicos de los usuarios'}

    id_user = db.Column(db.Integer, primary_key=True, autoincrement=True, info={'comment': 'Identificador único del usuario'})
    username = db.Column(db.String(50), nullable=False, unique=True, info={'comment': 'Nombre de usuario o cédula'})
    email = db.Column(db.String(256), nullable=False, unique=True, info={'comment': 'Correo electrónico del usuario'})
    password_hash = db.Column(db.String(128), nullable=False, info={'comment': 'Hash de la contraseña del usuario'})
    role = db.Column(db.String(50), nullable=False, info={'comment': 'Rol del usuario (ej. cliente, admin, vendedor)'})
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
