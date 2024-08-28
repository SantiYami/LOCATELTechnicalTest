from flask_restx import Api
from flask import Blueprint
from flask import render_template, request
import os

from .main.controller.user_controller import api as user_ns
from .main.controller.product_controller import api as product_ns
from .main.controller.sale_header_controller import api as sale_header_ns
from .main.controller.sale_detail_controller import api as sale_detail_ns

blueprint = Blueprint('api', __name__, static_folder='../templates/dist/static' , template_folder='../template')

api = Api(blueprint,
          title='API',
          version='1.0',
          description='flask restplus web service'
          )

# Exposición de los servicios al frontend
api.add_namespace(user_ns, path='/serv-user')
api.add_namespace(product_ns, path='/serv-product')
api.add_namespace(sale_header_ns, path='/serv-sale-header')
api.add_namespace(sale_detail_ns, path='/serv-sale-detail')

@blueprint.route('/')
def home():
    return render_template('dist/index.html')
