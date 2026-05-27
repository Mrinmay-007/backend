# db.py
from sqlalchemy import create_engine #type: ignore
from sqlalchemy.orm import sessionmaker, declarative_base #type: ignore

# Aiven MySQL Database URL

import os
from dotenv import load_dotenv #type: ignore

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
# Create engine with SSL enabled
engine = create_engine(
    DATABASE_URL,
    connect_args={
        "ssl": {
            "ssl_mode": "REQUIRED"
        }
    }
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()