from sqlalchemy import Column, String, Integer, ForeignKey, Date, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid
from database import Base

class MentalHealth(Base):
    __tablename__ = "Classification mental health"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    mood_swing = Column(Enum('NO', 'YES', name='mood_swing'))
    optimisim = Column(Enum('1 From 10', '2 From 10', '3 From 10', '4 From 10', '5 From 10', '6 From 10', '7 From 10', '8 From 10', '9 From 10',name='optimism'))
    euphoric = Column(Enum('Seldom', 'Most-Often', 'Usually', 'Sometimes',name='euphoric'))
    exhausted = Column(Enum('Sometimes', 'Usually', 'Seldom', 'Most-Often',name='exhausted'))
    concentration = Column(Enum('1 From 10', '2 From 10', '3 From 10', '4 From 10', '5 From 10', '6 From 10', '7 From 10', '8 From 10', '9 From 10',name='concentration'))
    sexual_activity = Column(Enum('1 From 10', '2 From 10', '3 From 10', '4 From 10', '5 From 10', '6 From 10', '7 From 10', '8 From 10', '9 From 10',name='sexual_activity'))
    aggressive_response = Column(Enum('NO', 'YES',name='aggressive_response'))
    suicidal_thoughts = Column(Enum('NO', 'YES',name='suicidal_thoughts'))
    authority_respect = Column(Enum('NO', 'YES',name='authority_respect'))
    sadness = Column(Enum('Usually', 'Sometimes', 'Seldom', 'Most-Often',name='sadness'))
    prediction=Column(String, nullable=False) 