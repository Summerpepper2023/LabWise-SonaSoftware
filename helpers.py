class User:
    def __init__(self, id:int, name:str, username:str, password:str, job:str):
        self.id = id
        self.name = name
        self.username = username
        self.password = password
        self.job = job
        
    def __str__(self):
        return (f"Id:{self.id}\nname:{self.name}\nusername:{self.username}\npassword:{self.password}\njob:{self.job}")
    
    @classmethod
    def get(cls):
        id = int(input("id: "))
        name = input("Name: ")
        username = input("username: ")
        password = input("Password: ")
        job = input("Job: ")
        return cls(id, name, username, password, job)

    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, id):
        if not id:
            raise ValueError("Invalid Id")
        self._id = id
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name
    
    @property
    def username(self):
        return self._username
    @username.setter
    def username(self,username):
        if not username:
            raise ValueError("Missing username")
        self._username = username
        
    @property
    def password(self):
        return self._password
    @password.setter
    def password(self,password):
        if not password:
            raise ValueError ("Missing password")
        self._password=password

    @property
    def job(self):
        return self._job
    @job.setter
    def job(self, job):
        jobs = ["Admin", "Analist", "BPM"]
        if not job or job not in jobs:
            raise ValueError("Invalid Job")
        self._job = job
    
    def Insert_db(self, db):
        # Insertar nuevo usuario a la base de datos
        return
    def Delete_db(self, db):
        # Eliminamos al usuario de la base de datos
        return
    def Update_db(self, db):
        # Actualiza la información del usuario en la base de datos
        return
