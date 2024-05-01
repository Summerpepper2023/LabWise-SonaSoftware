class User:
    
    jobs = ["admin", "analist", "BPM"]

    def __init__(self, user_id:int, name:str, username:str, password:str, job:str):
        self.__user_id = user_id
        self.name = name
        self.username = username
        self.password = password
        self.job = job
    
    def __str__(self):
        return f"User id: {self.__user_id}\nName: {self.name}\nUsername: {self.username}\nPassword: {self.password}\nJob: {self.job}"

    @classmethod
    def get(cls):
        user_id = int(input("User_id: "))
        name = input("Name: ")
        username = input("Username: ")
        password = input("Password: ")
        job = input("Job: ")
        
        return cls(user_id, name, username, password, job)
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing Name...")
        self._name = name
    
    @property
    def username(self):
        return self._username
    @username.setter
    def username(self, username):
        if not username:
            raise ValueError("Missing Username...")
        self._username = username
    
    @property
    def password(self):
        return self._password
    @password.setter
    def password(self, password):
        if not password:
            raise ValueError("Missing Password...")
        self._password = password
    
    @property
    def job(self):
        return self._job
    
    @job.setter
    def job(self, job):
        if job.lower() not in ["admin", "analist", "bpm"]:
            raise ValueError(f"Invalid Job {job} is not recognized as a valid job...")
        self._job = job
    
    def insert_users_db(self, db):
        ...
    def update_users_db(self, db):
        ...
    def delete_users_db(self, db):
        ...
