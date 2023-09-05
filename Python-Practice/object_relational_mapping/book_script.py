from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Person(Base):
    __tablename__ = "people"

    ssn = Column("ssn", Integer, primary_key=True)
    firstname = Column("firstname", String)
    lastname = Column("lastname", String)
    gender = Column("gender", CHAR)
    age = Column("age", Integer)

    def __init__(self, ssn, firstname, lastname, gender, age):
        self.ssn = ssn
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.age = age
    
    def __repr__(self):
        return f"({self.ssn}) {self.firstname} {self.lastname} ({self.gender}, {self.age})"
    
engine = create_engine("sqlite:///mydb.db", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

# person = Person(12312, "Chris", "Tendo", "M", 55)
# p1 = Person(57546, "Charles", "Rain", "M", 73)
# p2 = Person(33809, "Clivon", "Rain", "M", 25)
# p3 = Person(27400, "Onesmus", "Tendo", "M", 31)
# session.add(p1)
# session.add(p2)
# session.add(p3)
# session.commit()

# results = session.query(Person).all()
results = session.query(Person).filter(Person.lastname == "Tendo")

for r in results:
    print(r)
