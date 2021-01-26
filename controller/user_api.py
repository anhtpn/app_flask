from flask import Response, request, jsonify
from flask_restful import Resource

from model.user import User, Rating
import csv


class LoginApi(Resource):
    def get(self):
        # user = User()
        # user.username = "ducanh"
        # user.password = "123456"
        # user.save()
        users = User.objects
        return Response(users.to_json(), mimetype="application/json", status=200)

        # with open('ratings.csv', newline='') as csvfile:
        #     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        #     user_id = "1"
        #     list_rate = []
        #     user = User()

        #     for row in spamreader:
        #         user_list = row[0].split(",")
        #         if user_id != user_list[0]:
        #             user.id_user = user_id
        #             user.username = "BanAnh"
        #             user.password = "123456"
        #             user.rate = list_rate
        #             user.save()
        #             list_rate = []
        #             user = User()
        #             user_id = user_list[0]
        #         else:
        #             rate = Rating()
        #             rate.id_movie = user_list[1]
        #             rate.rating =  user_list[2]
        #             rate.timestamp =  user_list[3]
        #             list_rate.append(rate)
                
               

    def post(self):
        pass

class UserId(Resource):

    def get(self,user_id):
        user = User.objects.get(id_user = user_id)
        return Response(user.to_json(), mimetype="application/json", status=200)

