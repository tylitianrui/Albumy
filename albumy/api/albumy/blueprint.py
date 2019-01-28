# -*-coding:utf-8-*-

from flask import Blueprint
from flask_restful import Api

from albumy.api.albumy.albumy import Albumy

albumy_blueprint = Blueprint("albumy", __name__, url_prefix="/api")
albumy_api = Api(albumy_blueprint, prefix="/albumy",
               default_mediatype="application/json; charset=utf-8")

albumy_api.add_resource(Albumy, "","/<int:id>")


