from flask_restx import Api
from flask import Blueprint
from flask import render_template, request
import os

from .main.controller.inventory_controller import api as inventory_ns

blueprint = Blueprint('api', __name__, static_folder='../templates/dist/static' , template_folder='../template')

api = Api(blueprint,
          title='API',
          version='1.0',
          description='flask restplus web service'
          )

api.add_namespace(inventory_ns, path='/inventory')

@blueprint.route('/')
def home():
    return render_template('dist/index.html')
