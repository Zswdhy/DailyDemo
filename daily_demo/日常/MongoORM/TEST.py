from mongoengine import *

print(connect('tumblelog'))


class User(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
