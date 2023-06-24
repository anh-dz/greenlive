from sqlalchemy import create_engine, text
engine = create_engine("sqlite:///Databases.db")
with engine.connect() as connection:
    result = connection.execute(text('select "Connected"'))
    print(result.all())