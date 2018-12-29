# -*-coding:utf-8-*-
from flask import Blueprint
from flask_restful import Api

follower_blueprint = Blueprint("follower", __name__, url_prefix="/api")
follower_api = Api(follower_blueprint, prefix="/follower")

follower_api.add_resource(Follower, "/")
