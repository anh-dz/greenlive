from sqlalchemy.orm import Session
from connect import engine
session = Session(bind = engine) 
#add vao trong db
'''
link1 = Links_point(
    id = 2,
    address = "localhost:5000",
    start = time.time()
)
session.add_all([link1])
session.commit()
'''


#2 cach de query
#statement = select(Links_point).where(Links_point.id.is_(1))
#result = session.scalars(statement)

#
'''result = session.query(Links_point).filter_by(id = 1)
for link in result:
    print(link)'''

#update tu db
'''
linkduy = session.query(Links_point).filter_by(id=1).first()
linkduy.id = 2
session.commit()
'''

#xoa tu db
'''
linkduy = session.query(Links_point).filter_by(id=2).first()
session.delete(linkduy)
session.commit()
'''
# can than gap none khi query
'''
linkduy = session.query(Links_point).filter_by(id=1).first()
if linkduy is not None:
    session.delete(linkduy)
else:
    print("It's none")
session.commit()
'''