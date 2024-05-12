from flask_init import app
from flask_sqlalchemy import SQLAlchemy
import logging
from sqlalchemy import Column, String, LargeBinary
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import registry
from typing import Optional

class Base(DeclarativeBase):
    registry = registry(type_annotation_map={str: String(128)})

db = SQLAlchemy(model_class=Base)
app.config["SQLALCHEMY_DATABASE_URI"] = "mariadb+mariadbconnector://alledaags:geloven@127.0.0.1:3306/alledaags"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


# datatype mappings: https://docs.sqlalchemy.org/en/20/orm/declarative_tables.html#mapped-column-derives-the-datatype-and-nullability-from-the-mapped-annotation
# mapping multiple type configurations: https://docs.sqlalchemy.org/en/20/orm/declarative_tables.html#mapping-multiple-type-configurations-to-python-types

class Cache(db.Model):  # the key is lang.form
    key: Mapped[str] = mapped_column(primary_key=True)
    json: Mapped[bytes] = Column(LargeBinary(length=(2**32)-1))
    image: Mapped[Optional[bytes]] = Column(LargeBinary(length=(2**32)-1))


class Historical(db.Model):  # the key is the hash string (e.g. MzU5NjkwNTMzNTQ2Mjk=)
    hash: Mapped[str] = mapped_column(primary_key=True)
    data: Mapped[bytes]


class DailyFeed(db.Model):  # there's only one item at any time, key is "dailyfeed"
    __tablename__ = 'dailyfeed'
    key: Mapped[str] = mapped_column(primary_key=True)
    day: Mapped[str]
    title: Mapped[str]
    description: Mapped[str]
    url: Mapped[str]
    image_url: Mapped[str]
    pubDate: Mapped[str]


'''
from google.appengine.ext import ndb
import logging


class cache(ndb.Model):  # the key is lang.form
    json = ndb.TextProperty()
    image = ndb.BlobProperty()


class Historical(ndb.Model):  # the key is the hash string
    hash = ndb.StringProperty(required=True)
    data = ndb.TextProperty()

class Historical_futures():
    def __init__(self):
        self.l = []

    def add(self, f):
        self.l.append(f)

    def process(self):
        entities = []
        for f in self.l:
            entities.append(f.get_result())
        ndb.put_multi(entities)
        logging.info("Storing data for sharing link done")


class DailyFeed(ndb.Model):  # there's only one item at any time, key is "dailyfeed"
    day = ndb.StringProperty()
    title = ndb.StringProperty()
    description = ndb.StringProperty()
    url = ndb.StringProperty()
    image_url = ndb.StringProperty()
    pubDate = ndb.StringProperty()
'''
