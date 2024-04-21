class User:
    def __init__(self, user_id:int, name:str,  username:str, password:str, job:str):
        self.id = user_id
        self.username = username
        self.name = name
        self.password = password
        self.job = job
    
    def __str__(self):
        return f"Name:{self.name}, id:{self.id}, username:{self.username}, password:{self.password}, job:{self.job}"
    
    def enter_db(self):
        # Ingresamos al usuario  la base de datos de usuarios
        return
    
    def update_db(self):
        # Actualizamos la base dfe datos de usuarios
        return
    
    def delet_db(self):
        # Eliminamos el usuario de la base de datos de usuarios
        return

class Product:
    def __init__(self, product_id:int, name:str, quantity:str, temperature:float, batch:str, processes:list, presentation:str, inCharge:str):
        self.id = product_id
        self.name = name
        self.quantity = quantity
        self.temperature = temperature
        self.batch = batch
        self.processes = processes
        self.presentation = presentation
        self.inCharge = inCharge
    
    def __str__(self):
        return f"id: {self.id}, name:{self.name}, quantitiy:{self.quantity}, temperature:{self.temperature}, 
                batch:{self.batch}, process:{self.process}, presentatio:{self.presentation}, in charge:{self.inCharge}"

    def enter_db(self):
        # Ingresamos el usuario a la base de datos de usuarios
        return
    
    def update_db(self):
    # Actualizamos la informacion de la base de datos de usuarios
        return

    
    def delete_db(self):
        # Eliminamos el producto de la base de datos de usuarios
        return


class Certificate:
    def __init__(self, certificate_id:int, process:str, date:str, product_info:dict, inCharge:str):
        self.id = certificate_id
        self.process = process
        self.date = date
        self.product_info = product_info
        self.inCharge = inCharge
        self.approved = False
        self.pdf = None
        self.signature = None
    
    def __str__(self):
        return f"id:{self.id}, process:{self.process}, date:{self.date}, product info:{self.product_info}, in charge:{self.inCharge}"

    def generate_pdf(self, template):
        # Se genera el pdf del certificado basandose en un template y se añade a la base de datos, 
        # si ya una anterior version de este se elimina
        return 
    
    def aprove_certificate(self, pdf, signature):
        # Se incluye la firma del administrador en el archivo del certificado
        return
    
    def send_BPM(self, pdf):
        # Ingresamos el certificado a la base de datos del area de BPM
        return
    
    def return_certificate(self, pdf):
        # Cambiamos el estado de aprovado a False y se elimina de la base de BPM
        return
