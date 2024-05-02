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
    def get_user(cls):
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


class Product:

    presentations = ["ampolleta", "tabletas", "bioburden"]
    def __init__(self, register_number:str, product_name:str, active:str, description:str, batch_number:str, batch_size:int, presentation:str,
                 quantity:str, manufacture_date:str, due_date:str):
        
        self.__register_number = register_number
        self.product_name = product_name
        self.active = active
        self.description = description
        self.batch_number = batch_number
        self.batch_size = batch_size
        self.presentation = presentation
        self.quantity = quantity
        self.manufacture_date = manufacture_date
        self.due_date = due_date

    def __str__(self):
        return f"Register number:{self.__register_number}\nName:{self.product_name}\nActive:{self.active}\nDescription:{self.description}\nBatch_number:{self.batch_number}\nBatch Size:{self.batch_size}\nPresentation:{self.presentation}\nQuantitiy:{self.quantity}\nManufacture Date:{self.manufacture_date}\nDue Date:{self.due_date}"
    
    @classmethod
    def get_product(cls):
        register_number = input("Register Number: ")
        product_name = input("Name: ")
        active = input("Active: ")
        description = input("Description: ")
        batch_number = input("Bactch: ")
        batch_size = input("batch_size: ")
        presentation = input("presentation: ")
        quantity = input("quantity: ")
        manufacture_date = input("manufacture_date: ")
        due_date = input("due_date: ")

        return cls(register_number, product_name, active, description, batch_number, batch_size, presentation, quantity, manufacture_date, due_date)
    
    @property
    def product_name(self):
        return self._product_name
    @product_name.setter
    def product_name(self, name):
        if not name:
            raise ValueError("Missing Name...")
        self._product_name = name
    
    @property
    def active(self):
        return self._active
    @active.setter
    def active(self, active):
        if not active:
            raise ValueError("Missing Active...")
        self._active
    
    @property
    def description(self):
        return self._description
    @description.setter
    def description(self, description):
        if not description:
            raise ValueError("Missing Name...")
        self._description
    
    @property
    def batch_number(self):
        return self._batch_number
    @batch_number.setter
    def batch_number(self, number):
        if not number:
            raise ValueError("Missing Batch Number...")
        self._batch_number
    
    @property
    def batch_size(self):
        return self._batch_size
    @batch_size.setter
    def batch_size(self, size):
        if not size:
            raise ValueError("Missing Batch Size...")
        self._batch_size = size
    
    @property
    def presentation(self):
        return self._presentation
    @presentation.setter
    def presentation(self, presentation):
        presentations = ["ampolleta", "tabletas", "bioburden", "bolsa x 200ml", "tubo apirogeno x 30ml"]
        if not presentation or presentation not in presentations:
            raise ValueError("Invalid Presentation...")
        self._presentation = presentation
    
    @property
    def quantity(self):
        return self._quantity
    @quantity.setter
    def quantity(self, quantity):
        if not quantity:
            raise ValueError("Missing Quantity...")
        self.__quantity
    
    @property
    def manufacture_date(self):
        return self._manufacture_date
    @manufacture_date.setter
    def manufacture_date(self, date):
        if not date:
            raise ValueError("Missing Manufacture Date...")
        self._manufacture_date = date
    
    @property
    def due_date(self):
        return self._due_date
    @due_date.setter
    def due_setter(self, date):
        if not date:
            raise ValueError("Missing Due Date...")
    
    def insert_products_db(self, db):
        ...
    def update_products_db(self, db):
        ...
    def delete_products_db(self, db):
        ...