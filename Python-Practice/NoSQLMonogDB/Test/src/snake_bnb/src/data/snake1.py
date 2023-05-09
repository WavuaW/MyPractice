import mongoengine

class Snake:
    registered_date = mongoengine.DateTimeField()
    species = mongoengine.StringField()

    length = mongoengine.FloatField()
    name = mongoengine.StringField()
    is_venomous = mongoengine.BooleanField()

    meta = {
        'db_alias': 'core',
        'collection': 'snakes'
    }
