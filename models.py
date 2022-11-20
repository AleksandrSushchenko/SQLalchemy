import sqlalchemy as sq
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Publisher(Base):
    __tablename__ = 'publisher'
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), nullable=False)
    name2 = sq.Column(sq.String(length=40), nullable=False)

def create_tabeles(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)