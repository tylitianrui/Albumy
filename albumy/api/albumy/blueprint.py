# -*-coding:utf-8-*-

from flask import Blueprint
from flask_restful import Api

from albumy.api.albumy.albumy import Albumy
from albumy.api.albumy.others_albumy import OthersAlbumy

albumy_blueprint = Blueprint("albumy", __name__, url_prefix="/api")
albumy_api = Api(albumy_blueprint, prefix="/albumy",
               default_mediatype="application/json; charset=utf-8")

albumy_api.add_resource(Albumy, "","/<int:id>")

others_albumy_api = Api(albumy_blueprint, prefix="",
               default_mediatype="application/json; charset=utf-8")
others_albumy_api.add_resource(OthersAlbumy, "/<int:user_id>/albumy","/<int:user_id>/albumy/<int:id>")


