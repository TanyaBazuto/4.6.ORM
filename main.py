import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import create_tables, Publisher, Book, Stock, Shop, Sale

DSN = 'postgresql://postgres:nfnmzyf11-6886@localhost:5432/ORM'
engine = sqlalchemy.create_engine(DSN)
create_tables(engine)

# создание сессии
Session = sessionmaker(bind=engine)
session = Session()

# создание объектов
p1 = Publisher(name='Александр Пушкин')
p2 = Publisher(name='Федор Достоевский')

session.add_all([p1, p2])
session.commit()
print(p1.id, p2.id)



session.close()
