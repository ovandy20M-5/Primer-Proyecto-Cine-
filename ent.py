#from Date_format import DateFormat

class Movie():
    def __init__(self, id_movie, title = None, url=None, classification=None, create_all=None):
        self.id_movie = id_movie
        self.title = title
        self.url = url
        self.classification = classification
        self.create_all = create_all
        

    def to_JSON(self):
        return{
            'id':self.id_movie,
            'title':self.title,
            'ulr':self.url,
            'classification':self.classification,
        }

        # date =      O 'date':      --->     DateFormat.convert_date(self.date)

class User():
    def __init__(self, id_user, name = None, lastname=None, password=None, email=None, phone_number=None,):
        self.id_user = id_user
        self.name = name
        self.lastname = lastname
        self.password = password
        self.email = email
        self.phone_number = phone_number
        

class token():
    def __init__(self, id_token, key_code= None, user_id=None, user=None, create_all=None):
        self.id_token = id_token
        self.key_code = key_code
        self.user_id = user_id
        self.user = user
        self.create_all = create_all
