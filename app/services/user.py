from app.models.user import User

class UserService(object):
    def __init__(self):
        pass
       
    def users(self, id, password):   
        user = User(id, password)
        print(f"ID : {user.id}")
        print(f"PWD : {user.password}")
        
    
    
    
    
     