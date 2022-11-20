import sqlalchemy
from sqlalchemy.orm import sessionmaker

from models import create_tabeles

DSN = 'postgresql://postgres:1109@localhost:5432/dbalchemy'
engine = sqlalchemy.create_engine(DSN)

create_tabeles(engine)

Session = sessionmaker(bind=engine)
session = Session()




session.close()