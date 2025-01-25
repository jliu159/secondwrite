from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Set up the SQLite engine
engine = create_engine('sqlite:///events.db', echo=True)  # SQLite database file

# Base class for SQLAlchemy models
Base = declarative_base()

# Session maker
Session = sessionmaker(bind=engine)