from .Databases import Base
from .connect import engine
import logging, sqlalchemy
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.DEBUG)
print("Creating >>>")
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
print("Done!")