# db.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Replace with your actual DB details
# DATABASE_URL = "mysql+pymysql://root:0070100@localhost:3306/test_db"
# DATABASE_URL = "mysql+pymysql://root:0070100@localhost:3306/attendance"
# DATABASE_URL = "mysql+pymysql://root:0070100@localhost:3306/test"
DATABASE_URL = 'mysql+pymysql://root:ytJKwHJKdGLchjjlvZwcNMCjhOxexyAa@junction.proxy.rlwy.net:22751/railway'
# DATABASE_URL = "mysql+pymysql://root:kntPHUZcmuFGVTOrgvAwtCHaaQxLCjQP@metro.proxy.rlwy.net:57591/railway"
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    
