from flask import Response, request, jsonify
from flask_restful import Resource
# from code.Process import RecommendMovie


class ModelApi(Resource):
    def get(self, user_id):
        try:
            # res = RecommendMovie(user_id)
            res = []
            return res
        except Exception:
            res = {"mes" : "Not user"}
            return jsonify(res)