from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = "postgresql://usersql:password@localhost/sqldb"

# engine permite la conexión con la BD
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# es para activar la conexión con la BD, bind es para decirle por donde ir
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

###es para utilizar otros modelos
Base = declarative_base()
