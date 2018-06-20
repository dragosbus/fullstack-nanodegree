from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import Base, Restaurant, MenuItem


engine = create_engine('sqlite:///restaurantmenu.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

'''
res1 = Restaurant(name="Pizza")
session.add(res1)
session.commit()
'''

res2 = session.query(Restaurant).filter_by(id=2).one()
res2.name = 'Hamburger'
session.add(res2)
session.commit()


q = session.query(Restaurant).all()
for a in q:
    print(a.name)
