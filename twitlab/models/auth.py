from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()

class User(Base):
    __tablename__ = "AUser"

    id          = Column(Integer, primary_key=True)
    username    = Column(String)
    passwd      = Column(String)
    group_id    = Column(Integer, ForeignKey('AUser.id'))

    def __repr__(self):
        return "<User(id='%s', name='%s', passwd='%s', group='%s')>" % \
                    (self.id, self.username, self.passwd, self.group_id)
                    


class Group(Base):
    __tablename__ = "AGroup"

    id          = Column(Integer, primary_key=True)
    group_name  = Column(String)

    def __repr__(self):
        return "<Group(id='%s', name='%s')>" % \
                    (self.id, self.group_name)