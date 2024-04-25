class User:
    def __init__(self, user_id:int, name:str, username:str, password:str, job:str):
        self.user_id = user_id
        self.name = name
        self.username = username
        self.password = password
        self.job = job
        
    def __str__(self):
        return (f"Id:{self.id}\nname:{self.name}\nusername:{self.username}\npassword:{self.password}\njob:{self.job}")
    
    @classmethod
    def get(cls):
        user_id = int(input("id: "))
        name = input("Name: ")
        username = input("username: ")
        password = input("Password: ")
        job = input("Job: ")
        return cls(user_id, name, username, password, job)

    @property
    def user_id(self):
        return self._id
    @user_id.setter
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
        ...
    def Delete_db(self, db):
        # Eliminamos al usuario de la base de datos
        ...
    def Update_db(self, db):
        # Actualiza la información del usuario en la base de datos
        ...

class Transaction(User):
    def __init__(self, register_id:int,user_id:int, username:str, module_name:str, product_name:str,product_id:int, action:str):
        super().__init__(user_id, username)
        self.register_id = register_id
        self.module_name = module_name
        self.product_name = product_name
        self.product_id = product_id
        self.action = action
        
    def __str__(self):
        return f"User_id:{self.user_id}\nName:{self.name}\nRegister_id:{self.register_id}\nProduct_Name:{self.product_name}\nProduct_id:{self.product_id}\nDescription:{self.action}"
    
    @classmethod
    def get(cls):
        register_id = int(input("Ingrese el número de registro: "))
        user_id = int(input("Ingrese el id del usuario: "))
        username = input("Ingrese el username: ")
        module_name = input("Ingrese el modulo: ")
        product_name = input("Ingrese el nombre del producto:")
        product_id = input("Ingrese el numero de serie del producto: ")
        action = inptu("Ingrese la acción realizada")
        return cls(register_id, user_id, username, module_name, product_name, product_id, action)

    @property
    def register_id(self):
        return self._register_id
    @register_id.setter
    def register_id(self, id):
        if not id:
            raise ValueError("Missing Register ID")
        self._register_id = id
    
    @property
    def module_name(self):
        return self._module_name
    @module_name.setter
    def module_name(self, name):
        if not name:
            raise ValueError("Missing Module Name")
    
    @property
    def product_name(self):
        return self._product_name
    @product_name.setter
    def product_name(self, name):
        if not name:
            raise ValueError("Missing Product Name")
        self._product_name = name
    
    @property
    def product_id(self):
        return self._product_id
    @product_id.setter
    def product_id(self, id):
        if not id:
            raise ValueError("Missing Product Id")
    
    @property
    def action(self):
        return self._action
    @action.setter
    def action(self, action):
        actions = ["Registrate Product", "Delete Product", "Register Analisis", "Edit Certificate", "Approve Certificate", "Delete Certificate"]
        if not action:
          raise ValueError("Missing Action")
        self._action = action
    
    def Insert_db(self, db):
        # Insertar el registro de la transacción en la base de datos
        ...
    def Delete_db(self, db):
        # Eliminar el registro de la transacción de la base de datos
        ...

class Product():
    def __init__(self, product_id:int, id:int, name:str, quantity:float, measure:str, temperature:float, batch:str, process:str, presentation:str):
        self.product_id = product_id
        self.name = name
        self.quantity = quantity
        self.measure = measure
        self.temperature = temperature
        self.batch = batch
        self.process = process
        self.presentation = presentation
    
    def __init__(self):
        return f"Id:{self.id}\nName:{self.name}\nQuantity:{self.quantity}\nMeasure:{self.measure}\nTemperature:{self.temperature}\nBatch:{self.batch}\nProcess:{self.process}\nPresentation:{self.presentation}"
    
    @classmethod
    def get():
        product_id = int(input("Product_id: "))
        name = input("Product name: ")
        quantity = float(input("Product quantity: "))
        measure = input("Measure: ")
        temperature = float(input("Temperature"))
        batch = input("Product batch: ")
        process = input("Process: ")
        presentation = input("Presentation: 0")
        return cls(id, name, quantity, measure, temperature, batch, process, presentation)

    @property
    def product_id(self):
        return self.__id
    @product_id.setter
    def product_id(self, id):
        if not id:
            raise ValueError("Missing Id")
        self._product_id = id
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    @property
    def quantity(self):
        return self._quantity
    @quantity.setter
    def quantity(self, quantity):
        if not name:
            raise ValueError("Missing Quantity")

    @property
    def measure(self):
        return self._measure
    @measure.setter
    def measure(self, measure):
        measures:[]
        if not measure or measure not in measures:
            raise ValueError("Missing Measure or Invalid Measure")
        self._measure = measure

    @property
    def temperature(self):
        return self._temperature
    @temperature.setter
    def temperature(self, temperature):
        if not temperature:
            raise ValueError("Missing temperature")
        self._temperature = temperature

    @property
    def batch(self):
        return self._batch
    @batch.setter
    def batch(self, batch):    
        if not batch:
            raise ValueError("Missing Batch")
        self._batch = batch
    
    @property
    def process(self):
        return self._process
    @process.setter
    def process(self, process):
        processes = []
        if not process or process not in processes:
            raise ValueError("Missing or Invalid process")
        self._process = process
    
    @property
    def presentation(self):
        return self._presentation
    @presentation.setter
    def presentation(self, presentation):
        presentations = []
        if not presentation or presentation not in presentations:
            raise ValueError("Missing Presentation or Invalid Presentation")

    def insert_db(self, db):
        # Ingresamos el producto a la base de datos
        ...
    def update_db(self, db):
        # Actualizamos el producto en la base de datos
        ...
    def delete_db(self, db):
        # Eliminamos el producto de la base de datos
        ...
