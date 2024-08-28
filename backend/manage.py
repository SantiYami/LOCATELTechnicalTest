import os
import unittest
from faker import Faker
from flask.cli import FlaskGroup
from app import blueprint
from app.main import create_app, db
from app.main.model.user import User
from app.main.model.client_detail import ClientDetail
from app.main.model.session import Session
from app.main.model.product import Product
from app.main.model.sale import Sale
from app.main.model.sale_detail import SaleDetail

import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.register_blueprint(blueprint)

app.app_context().push()

cli = FlaskGroup(app)

fake = Faker()

# Crear tablas si no existen
@app.cli.command('seed-db')
def seed_db():
    """Seed the database with test data."""
    with app.app_context():
        # Limpia las tablas
        db.drop_all()
        db.create_all()

        # Genera un usuario admin estático
        admin_user = User(
            username='admin',
            email='admin@admin.com',
            role='admin'
        )
        admin_user.set_password('admin123')

        # Genera otros datos de prueba para User
        users = [admin_user]  # Empezamos con el admin
        for _ in range(10):
            user = User(
                username=fake.unique.ssn(),
                email=fake.unique.email(),
                role='client' if fake.boolean() else 'admin'
            )
            user.set_password(fake.password())
            users.append(user)

        db.session.add_all(users)
        db.session.commit()

        # Genera datos de prueba para ClientDetail
        client_details = []
        for user in users:
            client_detail = ClientDetail(
                id_user=user.id_user,
                name=fake.name(),
                address=fake.address(),
                phone=fake.phone_number()
            )
            client_details.append(client_detail)

        db.session.add_all(client_details)
        db.session.commit()

        # Genera datos de prueba para Product
        products = []
        for _ in range(10):
            product = Product(
                code=fake.unique.uuid4(),
                name=fake.word(),
                sale_value=str(fake.pydecimal(left_digits=4, right_digits=2, positive=True)),  # Convertir a cadena
                handles_iva=fake.boolean(),
                iva_percentage=str(fake.pydecimal(left_digits=2, right_digits=2, positive=True)) if fake.boolean() else None  # Convertir a cadena
            )
            products.append(product)

        db.session.add_all(products)
        db.session.commit()

        # Genera datos de prueba para Sale
        sales = []
        for _ in range(10):
            sale = Sale(
                consecutive=fake.unique.uuid4(),
                date=fake.date_time_between(start_date='-1y', end_date='now'),
                user_id=fake.random_element(elements=[user.id_user for user in users]),
                total_sale=str(fake.pydecimal(left_digits=5, right_digits=2, positive=True))  # Convertir a cadena
            )
            sales.append(sale)

        db.session.add_all(sales)
        db.session.commit()

        # Genera datos de prueba para SaleDetail
        sale_details = []
        for sale in sales:
            for _ in range(fake.random_int(min=1, max=5)):
                sale_detail = SaleDetail(
                    sale_id=sale.id_sale,
                    product_id=fake.random_element(elements=[product.id_product for product in products]),
                    product_value=str(fake.pydecimal(left_digits=4, right_digits=2, positive=True)),  # Convertir a cadena
                    iva_calculated=str(fake.pydecimal(left_digits=3, right_digits=2, positive=True)) if fake.boolean() else None  # Convertir a cadena
                )
                sale_details.append(sale_detail)

        db.session.add_all(sale_details)
        db.session.commit()

@cli.command()
def run():
    app.run(host='0.0.0.0', port=5000, debug=True)


@cli.command()
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    cli()