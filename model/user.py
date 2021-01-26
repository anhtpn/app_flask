import mongoengine_goodjson as gj
from mongoengine import *


class Rating(gj.EmbeddedDocument):
    id_movie = StringField()
    rating = StringField()
    timestamp = StringField()


class User(gj.Document):
    id_user = StringField()
    username = StringField()
    rate = ListField(EmbeddedDocumentField(Rating))
    password = StringField()
