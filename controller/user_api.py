from flask import Response, request, jsonify
from flask_restful import Resource

from model.user import User

class LoginApi(Resource):
    def get(self):
        user = User()
        user.username = "ducanh"
        user.password = "123456"
        user.save()
        users = User.objects
        return Response(users.to_json(), mimetype="application/json", status=200)
    
    def post(self):
        pass
