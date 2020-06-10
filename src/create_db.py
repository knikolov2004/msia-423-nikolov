import logging

logger = logging.getLogger(__name__)

import sqlalchemy as sql
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, String

import config.config as c
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
    instrumentalness = Column(Integer, unique=False, nullable=False)
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
    artist = Column(String(70), unique=False, nullable=False)
    track = Column(String(70), unique=False, nullable=False)

    def __repr__(self):
        return '<Features %r>' % self.id



def set_up_rds():
    """Creates an database with the specified columns and datatypes, can be local SQLite or RDS - changed from
    config file"""
    # set up mysql/sqlite connection

    if c.LOCAL_DB == False:
        logger.info("Creating RDS database:")
        try:
            engine = sql.create_engine(c.SQLALCHEMY_DATABASE_URI)
        except:
            logger.error("Cannot create RDS database. Check to make sure you are on NU's VPN!")
    else:
        logger.info("Creating local SQLlite database")
        try:
            engine = sql.create_engine(c.SQLITE_ENGINE_STRING)
        except:
            logger.error("Cannot create local database. Check if path specified exists.")

    # create the tracks table
    Base.metadata.create_all(engine)

    # create a db session
    Session = sessionmaker(bind=engine)
    session = Session()

    # delete from table if not empty
    try:
        session.execute('''DELETE FROM features''')
    except:
        pass

    session.commit()
    logger.info("Database successfully created!")
    session.close()
