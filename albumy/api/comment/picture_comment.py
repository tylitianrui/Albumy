# -*-coding:utf-8-*-

from albumy.common.restful import RestfulBase, success_response
from albumy.extensions import login_required
from albumy.models import Comment as CommentModel


class PhotoComment(RestfulBase):
    @login_required
    def get(self, photo_id):
        comments = CommentModel.query.filter_by(photo_id=photo_id, is_delete=False).all()
        if not comments:
            return success_response()
        _data = []
        for item in comments:
            cm = item.get_comment()
            _data.append(cm)
        return success_response(data=_data)
