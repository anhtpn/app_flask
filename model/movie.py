import mongoengine_goodjson as gj
from mongoengine import *

class Movie(gj.Document):
    id_movie = IntField()
    name = StringField()
    genres = ListField(StringField())