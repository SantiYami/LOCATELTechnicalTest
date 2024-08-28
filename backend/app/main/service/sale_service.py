from .. import db
from ..model.sale import Sale
from ..model.sale_detail import SaleDetail
from flask import jsonify

import logging
import traceback

def create_sale(data):
    try:
        new_sale = Sale(
            consecutive=data['consecutive'],
            date=data['date'],
            id_user=data['id_user'],
            total_sale=data['total_sale']
        )
        db.session.add(new_sale)
        db.session.commit()
        return {"message": "Sale created successfully"}, 201
    except Exception as e:
        logging.error(e)
        logging.error(traceback.format_exc())
        response = {
            "message": "Error: " + str(e),
        }
        return response, 500
    finally:
        db.session.close()

def get_sales():
    try:
        sales = Sale.query.all()
        sales_data = [
            {
                "id": sale.id_sale,
                "consecutive": sale.consecutive,
                "date": sale.date,
                "id_user": sale.id_user,
                "total_sale": str(sale.total_sale)  # Convertir a cadena para JSON
            } for sale in sales
        ]
        return jsonify(sales_data), 200
    except Exception as e:
        logging.error(e)
        logging.error(traceback.format_exc())
        response = {
            "message": "Error: " + str(e),
        }
        return response, 500
    finally:
        db.session.close()

def get_sale(id):
    try:
        sale = Sale.query.filter_by(id_sale=id).first_or_404()
        sale_data = {
            "id": sale.id_sale,
            "consecutive": sale.consecutive,
            "date": sale.date,
            "id_user": sale.id_user,
            "total_sale": str(sale.total_sale)  # Convertir a cadena para JSON
        }
        return jsonify(sale_data), 200
    except Exception as e:
        logging.error(e)
        logging.error(traceback.format_exc())
        response = {
            "message": "Error: " + str(e),
        }
        return response, 500
    finally:
        db.session.close()

def get_sales_by_date(start_date, end_date):
    try:
        sales = Sale.query.filter(Sale.date.between(start_date, end_date)).all()
        sales_data = [
            {
                "id": sale.id_sale,
                "consecutive": sale.consecutive,
                "date": sale.date,
                "id_user": sale.id_user,
                "total_sale": str(sale.total_sale)  # Convertir a cadena para JSON
            } for sale in sales
        ]
        return jsonify(sales_data), 200
    except Exception as e:
        logging.error(e)
        logging.error(traceback.format_exc())
        response = {
            "message": "Error: " + str(e),
        }
        return response, 500
    finally:
        db.session.close()

def create_sale_detail(data):
    try:
        new_sale_detail = SaleDetail(
            sale_id=data['sale_id'],
            product_id=data['product_id'],
            product_value=data['product_value'],
            calculated_iva=data['calculated_iva']
        )
        db.session.add(new_sale_detail)
        db.session.commit()
        return {"message": "Sale detail created successfully"}, 201
    except Exception as e:
        logging.error(e)
        logging.error(traceback.format_exc())
        response = {
            "message": "Error: " + str(e),
        }
        return response, 500
    finally:
        db.session.close()

def get_sale_detail(id):
    try:
        sale_detail = SaleDetail.query.filter_by(id_detail=id).first_or_404()
        sale_detail_data = {
            "id": sale_detail.id_detail,
            "sale_id": sale_detail.sale_id,
            "product_id": sale_detail.product_id,
            "product_value": str(sale_detail.product_value),  # Convertir a cadena para JSON
            "calculated_iva": str(sale_detail.calculated_iva)  # Convertir a cadena para JSON
        }
        return jsonify(sale_detail_data), 200
    except Exception as e:
        logging.error(e)
        logging.error(traceback.format_exc())
        response = {
            "message": "Error: " + str(e),
        }
        return response, 500
    finally:
        db.session.close()

def get_sale_details_by_sale_id(sale_id):
    try:
        sale_details = SaleDetail.query.filter_by(sale_id=sale_id).all()
        details_data = [
            {
                "id": detail.id_detail,
                "sale_id": detail.sale_id,
                "product_id": detail.product_id,
                "product_value": str(detail.product_value),  # Convertir a cadena para JSON
                "calculated_iva": str(detail.calculated_iva)  # Convertir a cadena para JSON
            } for detail in sale_details
        ]
        return jsonify(details_data), 200
    except Exception as e:
        logging.error(e)
        logging.error(traceback.format_exc())
        response = {
            "message": "Error: " + str(e),
        }
        return response, 500
    finally:
        db.session.close()