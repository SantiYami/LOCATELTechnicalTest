from .. import db
from ..model.product import Product
from flask import jsonify

import logging
import traceback

def create_product(data):
    try:
        new_product = Product(
            code=data['code'],
            name=data['name'],
            sale_value=data['sale_value'],
            handles_iva=data['handles_iva'],
            iva_percentage=data['iva_percentage'] if data['handles_iva'] else 0
        )
        db.session.add(new_product)
        db.session.commit()
        return {"message": "Product created successfully"}, 201
    except Exception as e:
        logging.error(e)
        logging.error(traceback.format_exc())
        response = {
            "message": "Error: " + str(e),
        }
        return response, 500
    finally:
        db.session.close()

def get_products():
    try:
        products = Product.query.all()
        products_data = [
            {
                "id": product.id_product,
                "code": product.code,
                "name": product.name,
                "sale_value": product.sale_value,
                "handles_iva": product.handles_iva,
                "iva_percentage": product.iva_percentage
            } for product in products
        ]
        return jsonify(products_data), 200
    except Exception as e:
        logging.error(e)
        logging.error(traceback.format_exc())
        response = {
            "message": "Error: " + str(e),
        }
        return response, 500
    finally:
        db.session.close()

def get_product(id):
    try:
        product = Product.query.filter_by(id_product=id).first_or_404()
        product_data = {
            "id": product.id_product,
            "code": product.code,
            "name": product.name,
            "sale_value": product.sale_value,
            "handles_iva": product.handles_iva,
            "iva_percentage": product.iva_percentage
        }
        return jsonify(product_data), 200
    except Exception as e:
        logging.error(e)
        logging.error(traceback.format_exc())
        response = {
            "message": "Error: " + str(e),
        }
        return response, 500
    finally:
        db.session.close()

def update_product(id, data):
    try:
        product = Product.query.filter_by(id_product=id).first_or_404()
        product.name = data.get('name', product.name)
        product.sale_value = data.get('sale_value', product.sale_value)
        product.handles_iva = data.get('handles_iva', product.handles_iva)
        product.iva_percentage = data.get('iva_percentage', product.iva_percentage) if product.handles_iva else 0
        db.session.commit()
        return {"message": "Product updated successfully"}, 200
    except Exception as e:
        logging.error(e)
        logging.error(traceback.format_exc())
        response = {
            "message": "Error: " + str(e),
        }
        return response, 500
    finally:
        db.session.close()

def delete_product(id):
    try:
        product = Product.query.filter_by(id_product=id).first_or_404()
        db.session.delete(product)
        db.session.commit()
        return {"message": "Product deleted successfully"}, 200
    except Exception as e:
        logging.error(e)
        logging.error(traceback.format_exc())
        response = {
            "message": "Error: " + str(e),
        }
        return response, 500
    finally:
        db.session.close()
