from sqlalchemy import create_engine
from os import path

from models import base

def create_database(db_path='sqlite:///movies.db'):
    engine = create_engine(db_path)
    base.metadata.create_all(engine)
    print("Database and tables created successfully.")

if __name__ == "__main__":
    create_database() if not path.exists('movies.db') else print("Database already exists.")
        
