<<<<<<< HEAD
from sqlalchemy import create_engine, text
engine = create_engine("sqlite:///control/Database/Databases.db")
with engine.connect() as connection:
    result = connection.execute(text('select "Connected"'))
=======
from sqlalchemy import create_engine, text
engine = create_engine("sqlite:///control/Database/Databases.db")
with engine.connect() as connection:
    result = connection.execute(text('select "Connected"'))
>>>>>>> 31214a3bc26fe888fd3acafeb5d466ee82a3a743
    print(result.all())