from sqlalchemy import create_engine , Column , Integer , Text, DateTime
from sqlalchemy.orm import declarative_base , sessionmaker

Base = declarative_base()

class QuestionsAndAnswers(Base):
    __tablename__ = "Questions and Answers"
    id = Column(Integer , primary_key=True)
    questions = Column(Text ,nullable=False)
    answers = Column(Text ,nullable=False)
    tags = Column(Text ,nullable=False)

class NotAnswerdQuestions(Base):
    __tablename__ = "Not Answerd Questions"
    id = Column(Integer , primary_key = True)
    questions = Column(Text , nullable=False)
engine = create_engine('sqlite:///chat.db' ,  echo=True)

Base.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine)
db_session = SessionLocal()