from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
Base = declarative_base()
engine = create_engine("sqlite://", echo=True, future=True)
Base.metadata.create_all(engine)
