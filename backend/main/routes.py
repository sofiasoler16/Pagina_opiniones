from main.resources.tipo_comida import TipoComidaResources
from main.resources.plato import PlatoResources
from main.resources.restaurante import RestauranteResources
from main.resources.usuario import UsuarioResources
from main.resources.opinion import OpinionResources

from flask_restful import Api

import main.resources as resources

api = Api()

def initialize_routes(api):
    import main.resources as resources

    api.add_resource(resources.TipoComidaResources, "/tipos_comida")
    api.add_resource(resources.PlatoResources, "/platos")
    api.add_resource(resources.RestauranteResources, "/restaurantes")
    api.add_resource(resources.UsuarioResources, "/usuarios")
    api.add_resource(resources.OpinionResources, "/opiniones")
