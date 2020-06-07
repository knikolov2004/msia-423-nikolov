import logging

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
logger = logging.getLogger(__file__)

import sqlalchemy as sql
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, String, MetaData

import pandas as pd

from config.config import RDS_ENGINE_STRING
from config.config import SQLITE_ENGINE_STRING, LOCAL_DB
from config.config import DINNER_RAW_LOCATION, PARTY_RAW_LOCATION, SLEEP_RAW_LOCATION, WORKOUT_RAW_LOCATION

Base = declarative_base()


class Features(Base):
    """Create a data model for the database to be set up for adding songs and song features """
    __tablename__ = "features"
    danceability = Column(Float, unique=False, nullable=False)
    energy = Column(Float, unique=False, nullable=False)
    key = Column(Integer, unique=False, nullable=False)
    loudness = Column(Float, unique=False, nullable=False)
    mode = Column(Integer, unique=False, nullable=False)
    speechiness = Column(Float, unique=False, nullable=False)
    acousticness = Column(Float, unique=False, nullable=False)
    instrumentalness = Column(Float, unique=False, nullable=False)
    liveness = Column(Float, unique=False, nullable=False)
    valence = Column(Float, unique=False, nullable=False)
    tempo = Column(Float, unique=False, nullable=False)
    type = Column(String(70), unique=False, nullable=False)
    id = Column(String(70), primary_key=True)
    uri = Column(String(70), unique=True, nullable=False)
    track_href = Column(String(70), unique=True, nullable=False)
    analysis_url = Column(String(70), unique=True, nullable=False)
    duration_ms = Column(Integer, unique=False, nullable=False)
    time_signature = Column(Integer, unique=False, nullable=False)
    playlist = Column(String(70), unique=False, nullable=False)

    def __repr__(self):
        return '<Features %r>' % self.id



def set_up_rds():
    """Creates an database with the specified columns and datatypes, can be local SQLite or RDS - changed from
    config file"""
    # set up mysql/sqllite connection

    if not LOCAL_DB:
        logger.info("Creating RDS database:")
        engine = sql.create_engine(RDS_ENGINE_STRING)
    else:
        logger.info("Creating local SQLlite database")
        engine = sql.create_engine(SQLITE_ENGINE_STRING)

    # create the tracks table
    Base.metadata.create_all(engine)

    # create a db session
    Session = sessionmaker(bind=engine)
    session = Session()
    session.commit()
    #
    # delete from table if not empty
    try:
        session.execute('''DELETE FROM features''')
    except:
        pass
    #
    # raw_data = [DINNER_RAW_LOCATION, PARTY_RAW_LOCATION, SLEEP_RAW_LOCATION]
    #
    session.close()
