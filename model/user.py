import mongoengine_goodjson as gj
from mongoengine import *

class User(gj.Document):
    id_user = IntField()
    id_movie = IntField()
    username = StringField()
    password = StringField()
    timestamp = IntField()

