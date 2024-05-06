#---------------------------------------------------------------------------------------------------------------
#                                            Class User
#---------------------------------------------------------------------------------------------------------------
class User:
    #We declare the avialable jobs for a user
    jobs = ["admin", "analist", "BPM"]

    #We declare the constructor method
    def __init__(self, user_id:int, name:str, username:str, password:str, job:str):
        self.__user_id = user_id
        self.name = name
        self.username = username
        self.password = password
        self.job = job
    
    #Print method
    def __str__(self):
        return f"User id: {self.__user_id}\nName: {self.name}\nUsername: {self.username}\nPassword: {self.password}\nJob: {self.job}"

    #Class method for asking user's attributes and construct the object
    @classmethod
    def get_user(cls):
        user_id = int(input("User_id: "))   
        name = input("Name: ")
        username = input("Username: ")
        password = input("Password: ")
        job = input("Job: ")
        
        return cls(user_id, name, username, password, job)
    
    #We declare the setters and getters of the properties (protected attributes)
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
        if not job or job.lower() not in ["admin", "analist", "bpm"]:
            raise ValueError(f"Invalid Job {job} is not recognized as a valid job...")
        self._job = job
    
    #We declare an instance method for inserting the user to the users's database
    def insert_users_db(self, db):
        ...
    #We declare an instance method for updating the user's information in the users's database
    def update_users_db(self, db):
        ...
    #We declare an instance method for deleting the user of the users's database
    def delete_users_db(self, db):
        ...

#---------------------------------------------------------------------------------------------------------------
#                                            Class Manufacturer
#---------------------------------------------------------------------------------------------------------------
class Manufacturer:
    #We declare the contructor method
    def __init__(self, manufacturer_id, name, address):
        self.__manufacturer_id = manufacturer_id
        self.manufacturer_name = name
        self.manufacturer_address = address
    
    #We declare the print method
    def __str__(self):
        return f"Id:{self.__manufacturer_id}\nName:{self.manufacturer_name}\nAddress:{self.manufacturer_address}"
    
    #We declare a get method
    @classmethod
    def get_manufacturer(cls):
        manufacturer_id = int(input("manufacturer_id: "))
        manufacturer_name = input("name: ")
        manufacturer_address = input("address: ")
        return cls(manufacturer_id, manufacturer_name, manufacturer_address)
    
    #We declare the getters and setters
    @property
    def manufacturer_name(self):
        return self._manufacturer_name
    @manufacturer_name.setter
    def manufacturer_name(self, name):
        if not name:
            raise ValueError("Missing Manufacturer Name...")
        self._manufacturer_name = name
    
    @property
    def manufacturer_address(self):
        return self._manufacturer_address
    @manufacturer_address.setter
    def manufacturer_address(self, address):
        if not address:
            raise ValueError("Missing Manufacturer Address...")
        self._manufacturer_address = address
    
    #We declare an instance method for inserting the manufacturer to the manufacturers's database
    def insert_manufact_db(self, db):
        ...
    #We declare an instance method for updating the manufacturer's info in the manufacturers's database
    def update_manufact_db(self, db):
        ...
    #We declare an instance method for deleting the manufacturer from the manufacturers's database
    def delete_manufact_db(self, db):
        ...

#---------------------------------------------------------------------------------------------------------------
#                                            Class Client
#---------------------------------------------------------------------------------------------------------------
class Client:
    #We declare the contructor
    def __init__(self, client_id:int, name:str, address:str):
            self.__client_id  = client_id
            self.client_name = name
            self.client_address = address

    #We declare the print method
    def __str__(self):
         return f"Client Id:{self.__client_id}\nName:{self.client_name}\nAddress:{self.client_address}"
    
    #We declare the get method
    @classmethod
    def get_client(cls):
            client_id = int(input("Client id: "))
            client_name = input("Client Name: ")
            client_address = input("Clien Address: ")
            return cls(client_id, client_name, client_address)
    
    #We declare setters and getters
    @property
    def client_name(self):
        return self._client_name
    @client_name.setter
    def client_name(self, name):
        if not name:
            raise ValueError("Missing Client Name...")
        self._client_name = name

    @property
    def client_address(self):
        return self._client_address
    @client_address.setter
    def client_address(self, address):
        if not address:
            raise ValueError("Missing Client Address...")
        self._client_address = address
    
    #We declare an instance method for inserting the client to the client's database
    def insert_clients_db(self, db):
        ...
    #We declare an instance method for updating the client's information from the client's database  
    def update_clients_db(self, db):
        ...
    #We declare an instance method for deleting the client of the client's database
    def delete_clients_db(self, db):
        ...

#---------------------------------------------------------------------------------------------------------------
#                                          SubClass Transaction_Register
#---------------------------------------------------------------------------------------------------------------
class Transaction_Register(User):

    actions = ["delete product", "insert product", "edit product", "insert machine", "edit machine", "delete machine",
               "insert client", "edit client", "delete client", "insert manufacturer", "edit manufacturer", "delete manufacturer",
               "generate certificate", "edit certificate", "approve certificate"]
    
    def __init__(self, user_id:int, username:str, job:str, transaction_id:int, action:str, description:str,
                 date:str, hour:str, name:str="disabled", password:str="disabled"):
                  
        super().__init__(user_id, name, username, password, job)
        self.__transaction_id = transaction_id
        self.action = action
        self.description = description
        self.date = date
        self.hour = hour
    
    def __str__(self):
        return f"Username:{self.username}\nUser Job:{self.job}\nTransaction id:{self.__transaction_id}\nAction:{self.action}\nDescription:{self.description}\nDate:{self.date}\nHour:{self.hour}"
    
    @classmethod
    def get_transaction(cls):
        user_id = int(input("user_id: "))
        username = input("username: ")
        job = input("job: ")
        transaction_id = input("transaction_id: ")
        action = input("action: ")
        description = input("description: ")
        date = input("date: ")
        hour = input("hour:")

        return cls(user_id, username, job, transaction_id, action, description, date, hour)

    @property
    def action(self):
        return self._action
    @action.setter
    def action(self, action):
        actions = ["delete product", "insert product", "edit product", "insert machine", "edit machine", "delete machine",
               "insert client", "edit client", "delete client", "insert manufacturer", "edit manufacturer", "delete manufacturer",
               "generate certificate", "edit certificate", "approve certificate"]
              
        if not action or action.lower() not in actions:
            raise ValueError(f"Invalid Action {action}...")
        self._action = action
    
    @property
    def description(self):
        return self._description
    @description.setter
    def description(self, description):
        if not description:
            raise ValueError("Missing description...")
        self._description = description
    
    @property
    def date(self):
        return self._date
    @date.setter
    def date(self, date):
        if not date:
            raise ValueError("Missing date...")
        self._date = date
    
    @property
    def hour(self):
        return self._hour
    @hour.setter
    def hour(self, hour):
        if not hour:
            raise ValueError("Missing hour...")
        self._hour = hour
    
    def insert_transactions_db(self, db):
        ...
    def update_transactions_db(self, db):
        ...
    def delete_transactions_db(self, db):
        ...

#---------------------------------------------------------------------------------------------------------------
#                                            Class Product
#---------------------------------------------------------------------------------------------------------------
class Product(Client, Manufacturer):
    #We declare a class variable that storages the avialable presentations of a product.
    presentations = ["ampolleta", "tabletas", "bioburden"]

    #We declare the constructor method
    def __init__(self, product_id:str, product_name:str, active:str, description:str, batch_number:str, batch_size:int, presentation:str,
                 quantity:str, manufacture_date:str, due_date:str, client_name:str, client_address:str, manufacturer_name:str, manufacturer_address:str):  
        self.__product_id = product_id
        self.product_name = product_name
        self.active = active
        self.description = description
        self.batch_number = batch_number
        self.batch_size = batch_size
        self.presentation = presentation
        self.quantity = quantity
        self.manufacture_date = manufacture_date
        self.due_date = due_date
        self.client_name = client_name
        self.client_address = client_address
        self.manufacturer_name = manufacturer_name
        self.manufacturer_address = manufacturer_address

    #We declare a print method
    def __str__(self):
        return f"Register number:{self.__product_id}\nName:{self.product_name}\nActive:{self.active}\nDescription:{self.description}\nBatch_number:{self.batch_number}\nBatch Size:{self.batch_size}\nPresentation:{self.presentation}\nQuantitiy:{self.quantity}\nManufacture Date:{self.manufacture_date}\nDue Date:{self.due_date}\nClient_name:{self.client_name}\nClient Address:{self.client_address}\nManufcaturer name:{self.manufacturer_name}\nManufacturer address:{self.manufacturer_address}"
    
    #We declare a class method to get the product's attributes
    @classmethod
    def get_product(cls):
        product_id = int(input("Register Number: "))
        product_name = input("Name: ")
        active = input("Active: ")
        description = input("Description: ")
        batch_number = input("Batch: ")
        batch_size = input("batch_size: ")
        presentation = input("presentation: ")
        quantity = input("quantity: ")
        manufacture_date = input("manufacture_date: ")
        due_date = input("due_date: ")
        client_name = input("client name: ")
        client_address = input("Client Address: ")
        manufacturer_name = input("Manufacturer name: ")
        manufacturer_address = input("Mnufacturer Address: ")

        return cls(product_id, product_name, active, description, batch_number, batch_size, presentation, quantity, 
                   manufacture_date, due_date, client_name, client_address, manufacturer_name, manufacturer_address)
    
    #We declare the setters and getters of the properties (protected attributes)
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
        self._active = active
    
    @property
    def description(self):
        return self._description
    @description.setter
    def description(self, description):
        if not description:
            raise ValueError("Missing Name...")
        self._description = description
    
    @property
    def batch_number(self):
        return self._batch_number
    @batch_number.setter
    def batch_number(self, number):
        if not number:
            raise ValueError("Missing Batch Number...")
        self._batch_number = number
    
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
        presentations = ["ampolleta", "tableta", "bioburden", "bolsa x 200ml", "tubo apirogeno x 30ml"]
        if not presentation or presentation.lower() not in presentations:
            raise ValueError(f"{presentation} is not recognized as a valid presentation...")
        self._presentation = presentation
    
    @property
    def quantity(self):
        return self._quantity
    @quantity.setter
    def quantity(self, quantity):
        if not quantity:
            raise ValueError("Missing Quantity...")
        self._quantity = quantity
    
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
    def due_date(self, date):
        if not date:
            raise ValueError("Missing Due Date...")
        self._due_date = date
    
    #We declare an instance method for inserting the product to the products's database
    def insert_products_db(self, db):
        ...
    #We declare an instance method for updating the product's information in the products's database
    def update_products_db(self, db):
        ...
    #We declare an instance method for deleting the product of the products's database
    def delete_products_db(self, db):
        ...

#---------------------------------------------------------------------------------------------------------------
#                                            Class Product Register
#---------------------------------------------------------------------------------------------------------------
class Product_register(Product):
    def __init__(self, register_id:int, entrance_date:str, entrance_inCharge:str, analysis_purpose:str, entrance_temp:str, analysis:str,
                 analysis_init_date:str, analyisis_end_date:str, analist_inCharge:str, certificate_date:str, certificate_id:str,
                 product_id:str, product_name:str, active:str, description:str, batch_number:str, batch_size:str, presentation:str, quantity:str,
                 manufacture_date:str, due_date:str, client_name:str, client_address:str, manufacturer_name:str, manufacturer_address:str):
        
        super().__init__(product_id, product_name, active, description, batch_number, batch_size, presentation, quantity, manufacture_date,
                         due_date, client_name, client_address, manufacturer_name, manufacturer_address)
        
        self.__register_id = register_id
        self.entrance_date = entrance_date
        self.entrance_inCharge = entrance_inCharge
        self.analysis_purpose = analysis_purpose
        self.entrance_temp = entrance_temp
        self.analysis = analysis
        self.analysis_init_date = analysis_init_date
        self.analysis_end_date = analyisis_end_date
        self.analist_inCharge = analist_inCharge
        self.certificate_date = certificate_date
        self.certificate_id = certificate_id
    
    def __str__(self):
        return f"Register_id:{self.__register_id}\nEntrance date:{self.entrance_date}\nEntrance inCharge:{self.entrance_inCharge}\nAnalysis Purpose:{self.analysis_purpose}\nEntrance temp:{self.entrance_temp}\nAnalysis:{self.analysis}\nAnalysisi_init_date:{self.analysis_init_date}\nAnalysis end date:{self.analysis_end_date}\nAnalist_incharge:{self.analist_inCharge}\nCertificate date:{self.certificate_date}\nCertificate id:{self.certificate_id}"
    
    @classmethod
    def get_ProductRegister(cls):
        register_id = int(input("register_id: "))
        entrance_date = input("entrance_date: ")
        entrance_inCharge = input("entrance_inCharge: ")
        analysis_purpose = input("analysis_purpose: ")
        entrance_temp = input("entrance_temp: ")
        analysis = input("analysis: ")
        analysis_init_date = input("analysis_init_date: ")
        analysis_end_date = input("analyisis_end_date: ")
        analist_inCharge = input("analist_inCharge: ")
        certificate_date = input("certificate_date: ")
        certificate_id = input("certificate_id: ")
        product_id = input("product_id: ")
        product_name = input("Product name: ")
        active = input("active: ")
        description = input("description: ")
        batch_number = input("batch number: ")
        batch_size = input("batch size: ")
        presentation = input("presentation: ")
        quantity = input("quantity: ")
        manufacture_date = input("manufacture date: ")
        due_date = input("due date: ")
        client_name = input("client name: ")
        client_address = input("client address: ")
        manufacturer_name = input("manufacture name: ")
        manufacturer_address = input("manufacture address: ")

        return cls(register_id, entrance_date, entrance_inCharge, analysis_purpose, entrance_temp, analysis, analysis_init_date,
                   analysis_end_date, analist_inCharge, certificate_date, certificate_id, product_id, product_name, active, description,
                   batch_number, batch_size, presentation, quantity, manufacture_date, due_date, client_name, client_address,
                   manufacturer_name, manufacturer_address)
    
    @property
    def entrance_date(self):
        return self._entrance_date
    @entrance_date.setter
    def entrance_date(self, date):
        if not date:
            raise ValueError("Missing Entrance Date...")
        self._entrance_date = date

    @property
    def entrance_inCharge(self):
        return self._entrance_inCharge
    @entrance_inCharge.setter
    def entrance_inCharge(self, name):
        if not name:
            raise ValueError("Missing Entrance inCharge Name...")
        self._entrance_inCharge = name
    
    @property
    def analysis_purpose(self):
        return self._analysis_purpose
    @analysis_purpose.setter
    def analysis_purpose(self, purpose):
        if not purpose:
            raise ValueError("Missing Analysis Purpose...")
        self._analysis_purpose = purpose
    
    @property
    def entrance_temp(self):
        return self._entrance_temp
    @entrance_temp.setter
    def entrance_temp(self, temp):
        if not temp:
            raise ValueError("Missing Entrance Temp...")
        self._entrance_temp = temp
    
    @property
    def analysis(self):
        return self._analysis
    @analysis.setter
    def analysis(self, analysis):
        if not analysis:
            raise ValueError("Missing Analysis...")
        self._analysis = analysis
        
    @property
    def analysis_init_date(self):
        return self._analysis_init_date
    @analysis_init_date.setter
    def analysis_init_date(self, date):
        if not date:
            raise ValueError("Missing analysis init date...")
        self._analysis_init_date = date

    @property
    def analysis_end_date(self):
        return self._analysis_end_date
    @analysis_end_date.setter
    def analysis_end_date(self, date):
        if not date:
            raise ValueError("Missing analysis end date...")
        self._analysis_end_date = date
    
    @property
    def analist_inCharge(self):
        return self._analist_inCharge
    @analist_inCharge.setter
    def analist_inCharge(self, name):
        if not name:
            raise ValueError("Missing analist in charge name...")
        self._analist_inCharge = name
    
    @property
    def certificate_date(self):
        return self._certificate_date
    @certificate_date.setter
    def certificate_date(self, date):
        if not date:
            raise ValueError("Missing certificate date...")
        self._certificate_date = date
    
    @property
    def certificate_id(self):
        return self._certificate_id
    @certificate_id.setter
    def certificate_id(self, id):
        if not id:
            raise ValueError("Missing certificate id...")
        self._certificate_id = id
        
    
    def insert_registers_db(self, db):
        ...
    def update_registers_db(self, db):
        ...
    def delte_inserts_db(self, db):
        ...
#---------------------------------------------------------------------------------------------------------------
#                                            Class Machine
#---------------------------------------------------------------------------------------------------------------
class Machine:

    #We declare the constructor method
    def __init__(self, machine_name:str, machine_id:int, operator:str, reference:str, branch:str):
        self.machine_name = machine_name
        self.__machine_id = machine_id
        self.operator = operator
        self.reference = reference
        self.branch = branch

    #We declare the print method
    def __str__(self):
        return (f"\nMachin Id:{self.__machine_id}\nMachine Name:{self.machine_name}\nOperator:{self.operator}\nReference:{self.reference}\nBranch:{self.branch}")
    
    #We declare a class method to get the machine's attributes
    @classmethod
    def get_machine(cls):
        machine_id = int(input("Machine id: "))
        machine_name = input("Machine name: ")
        operator = input("Operator: ")
        reference = input("Reference: ")
        branch = input("Branch: ")
        return cls(machine_name, machine_id, operator, reference, branch)
    
    #We declare the setters and getters of the properties (protected attributes)
    @property
    def machine_name(self):
        return self._machine_name
    @machine_name.setter
    def machine_name(self, name):
        if not name:
            raise ValueError("Missing name...")
        self._machine_name = name
    
    @property
    def operator(self):
        return self._operator
    @operator.setter
    def operator(self, operator):
        if not operator:
            raise ValueError("Missing operator...")
        self._operator = operator 
    
    @property
    def reference(self):
        return self._reference
    @reference.setter
    def reference(self, reference):
        if not reference:
            raise ValueError("Missing reference...")
        self._reference = reference
    
    @property
    def branch(self):
        return self._branch
    @branch.setter
    def branch(self, branch):
        if not branch:
            raise ValueError("Missing branch...")
        self._branch = branch
    
    #We declare an instance method for inserting the machine to the machines's database
    def insert_machines_db(self, db):
        ...
    #We declare an instance method for updating the machine's information in the machines's database
    def update_machines_db(self, db):
        ...
    #We declare an instance method for deleting the machine of the machines's database
    def delete_machines_db(self, db):
        ...