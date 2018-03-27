#!/usr/bin/python3
"""
Creating class DBStorage to store objects in a MySQL Database
"""
from models.base_model import BaseModel
from models.state import State
from models.city import City
from os import environ
from sqlalchemy import create_engine, drop_all
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """
    Database storage class
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        Initializing an instance of db storage
        """
        user = environ('HBNB_MYSQL_USER')
        password = environ.get('HBNB_MYSQL_PWD')
        hostname = environ.get('HBNB_MYSQL_HOST')
        db_name = environ.get('HBNB_MYSQL_DB')
        connection = 'mysql+mysqldb://{}:{}@{}/{}'
        self.__engine = create_engine(connection.format(user, password,
                                                        hostname, db_name),
                                      pool_pre_ping=True)
        self.reload()
        if environ.get('HBNB_ENV') == 'test':
            self.__engine.drop_all()

    def all(self,  cls=None):
        """
        Querying all items in a db by class
        :param cls: the class to be checked
        :return: return a dictionary of all objects found
        """
        if cls is None:
            search = self.__session.query(User, State, City, Amenity, Place,
                                         Review)

        else:
            search = self.__session.query(cls)
        instance_dict = {}
        for found in search:
                key = found.__cls__.__name__ + '.' + found.id
                instance_dict[key] = found
        return instance_dict

    def new(self, obj):
        """
        Add a new object to db
        :param obj: object to be added
        """
        self.__session.add(obj)
        # self.save()

    def save(self):
        """
        commit all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        delete from the current database session, the object
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        create all tables in the database
        """
        Base.metadata.create_all(engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
