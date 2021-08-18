from datetime import datetime

class User:
    #Class atribute exmaple
    type = "normal"

    #overload, constructor, default values, *args, *kwargs
    def __init__(self, id=0, username='', email='', password=b'', fname='', lname='', dob=datetime.min):
        #private attributes
        # self.__id = id
        #oop or pythonic way  https://www.datacamp.com/community/tutorials/property-getters-setters
        #pythonic way, you don't need getters and setters
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.fname = fname
        self.lname = lname
        self.dob = dob

    #link https://python.plainenglish.io/flask-crud-application-using-mvc-architecture-3b073271274f
    @property
    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'password': self.password,
            'fname': self.fname,
            'lname': self.lname,
            'dob': self.dob
        }

    def __str__(self):
        return f"id: {self.id}\nusername: {self.username}\nemail: {self.email}\npassword: {self.password}\nfname: {self.fname}\nlname: {self.lname}\ndob: {self.dob}"

    