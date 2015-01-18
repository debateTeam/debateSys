from mongoengine import *
connect('my_db')
 
class User(Document):
    username = StringField(required=True)
    website = URLField()
    tags = ListField(StringField(max_length=16))


class Blog(Document):
	name = StringField(required = True)
	wesite = URLField()
	content = StringField(required = True)