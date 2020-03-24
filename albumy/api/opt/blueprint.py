from flask import Blueprint
from flask_restful import Api

from albumy.api.opt.pong import Pong

opt_blueprint = Blueprint("opt", __name__)
opt_api = Api(opt_blueprint,  prefix="",
              default_mediatype="application/json; charset=utf-8")
opt_api.add_resource(Pong, "/ping")
