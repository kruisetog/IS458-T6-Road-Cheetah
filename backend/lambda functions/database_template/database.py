""" Starts a session for the DB call """

# from pgsql.database import SessionLocal
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import Column, String, DateTime, Float


# connection
DATABASE_URL = "mysql+pymysql://admin:11111111@database-1-instance-1.cqbbxkouucyk.us-east-1.rds.amazonaws.com:3306/cs301_scis_bank"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_session():
    """ Creates a db session """
    try:
        _db = SessionLocal()
        return _db
    finally:
        _db.close()

#table / model


class User(Base):
    """" just declaring class """
    __tablename__ = 'user'

    User_ID: str = Column(String, primary_key=True)
    Points_Total: float = Column(Float)
    Miles_Total: float = Column(Float)
    Cashback_Total: float = Column(Float)
    # type: str = Column(String)
    # content: str = Column(String)
    # importance: str = Column(String, default="low")
    # email: str = Column(String)
    # status: str = Column(String, default="unread")
    # date_created: datetime = Column(DateTime, default=datetime.now)
    # date_modified: datetime = Column(DateTime, default=datetime.now)
