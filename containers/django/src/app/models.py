from mongoengine import *

class AppMongoSample(Document):
    longstring = StringField(max_length=500)
    shortstring = StringField(max_length=20)
