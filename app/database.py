from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker



engine = create_engine("mysql+mysqlconnector://root:@localhost:3306/Auth_sys", echo=True)
Base = declarative_base()
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
