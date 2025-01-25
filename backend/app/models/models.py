from sqlalchemy import Column, Integer, String, Text
from database.database import Base

# Define SQLAlchemy models that correspond to the protobuf messages
class Process(Base):
    __tablename__ = 'processes'
    id = Column(Integer, primary_key=True)
    parent_process_id = Column(Integer)
    process_id = Column(Integer)
    start_time = Column(Text)
    user_id = Column(Integer)
    application_id = Column(Integer)

class Application(Base):
    __tablename__ = 'applications'
    id = Column(Integer, primary_key=True)
    pe_file_id = Column(Integer)
    name = Column(String)
    vendor = Column(String)
    version = Column(String)

class PeFile(Base):
    __tablename__ = 'pe_files'
    id = Column(Integer, primary_key=True)
    sha256 = Column(String)
    name = Column(String)
    path = Column(String)
    modified_time = Column(Text)
    version = Column(String)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    security_identifier = Column(String)
    username = Column(String)
    domain = Column(String)

class Message(Base):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True)
    process_ids = Column(Text)
    application_ids = Column(Text)
    pe_file_ids = Column(Text)
    user_ids = Column(Text)