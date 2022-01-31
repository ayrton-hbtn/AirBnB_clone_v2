#!/usr/bin/python3
"""
    DB - Storage
"""

from sqlalchemy import create_engine
from models.base_model import Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.state import State
from models.user import User
from os import getenv


dict_class = {"Amenity": Amenity,
              "City": City,
              "Place": Place,
              "Review": Review,
              "State": State,
              "User": User}


class DBStorage:
    """ DBStorage """
    __engine = None
    __session = None

    def __init__(self):
        """ __init__ """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(getenv('HBNB_MYSQL_USER'),
                                             getenv('HBNB_MYSQL_PWD'),
                                             getenv('HBNB_MYSQL_HOST'),
                                             getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)

        if getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ all """
        dicto = {}
        if cls is None:
            for c in dict_class.values():
                for s in self.__session.query(c).all():
                    k = type(s).__name__ + "." + s.id
                    dicto[k] = s
        else:
            for s in self.__session.query(cls).all():
                k = type(s).__name__ + "." + s.id
                dicto[k] = s
        return dicto

    def new(self, obj):
        """add obj to the current database session."""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database and initialize session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """close session"""
        self.__session.close()
