from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
        
    __tablename__ = "user"
    
    id = Column (Integer, primary_key=True)
    username = Column (String)
    password = Column (String)
    
    def __repr__(self):
        return "Username: {}, Password: ******".format(self.username)
    

def main ():
    engine = create_engine('sqlite:///:memory:', echo=False)
    
    Base.metadata.create_all(engine)
    
    user1 = User("user1", "password1")
    print (user1)
    
main()