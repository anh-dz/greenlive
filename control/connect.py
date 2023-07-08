from sqlalchemy import create_engine, text
engine = create_engine("sqlite:///control/Database/Databases.db", pool_size=20)
with engine.connect() as connection:
    result = connection.execute(text('select "Connected"'))
print(result.all())