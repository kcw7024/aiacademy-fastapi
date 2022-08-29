from app.models.user import User

class UserService(object):
    def __init__(self):
        pass
       
    def login(self, id, password):   
        user = User(id, password)
        print(f"ID : {user.id}")
        print(f"PWD : {user.password}")
        
    
    
    
    
     