
#!/usr/bin/python3
"""
Creating class DBStorage to store objects in a MySQL Database
"""
from models import classes
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from os import getenv
from sqlalchemy import create_engine
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
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        hostname = getenv('HBNB_MYSQL_HOST')
        db_name = getenv('HBNB_MYSQL_DB')
        connection = 'mysql+mysqldb://{}:{}@{}/{}'
        self.__engine = create_engine(connection.format(user, password,
                                                        hostname, db_name),
                                      pool_pre_ping=True)
        self.reload()
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Querying all items in a db by class
        :param cls: the class to be checked
        :return: return a dictionary of all objects found
        """
        print("inside db")
        if cls is None:
            target_classes = list(classes.values())
        elif cls is not None and cls in classes:
            target_classes = [classes[cls]]

        instance_dict = {}
        for each_class in target_classes:
            try:
                loaded_objects = self.__session.query(each_class).all()
            except:
                continue
            for each_object in loaded_objects:
                key = "{}.{}".format(each_object.__class__.__name__, each_object.id)
                instance_dict[key] = each_object
        return instance_dict

    def new(self, obj):
        """
        Add a new object to db
        :param obj: object to be added
        """
        self.__session.add(obj)

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
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
        
