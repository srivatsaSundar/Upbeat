from sqlalchemy import Column, String, Integer, ForeignKey, Date, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid
from database import Base

# ORM Model for Profile
class Profile(Base):
    __tablename__ = "profiles"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    dob = Column(Date)
    gender = Column(Enum('male', 'female', 'other', name='gender_type'))
    appointment_frequency = Column(Enum('weekly', 'monthly', name='appt_frequency'))

    class Config:
        orm_mode = True
        from_attributes = True

# ORM Model for Doctor
class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    profile_id = Column(UUID(as_uuid=True), ForeignKey('profiles.id'))
    name = Column(String)
    phone_number = Column(String)
    clinic_or_hospital_name = Column(String)
    email = Column(String)

    profile = relationship("Profile", backref="doctors")

    class Config:
        orm_mode = True
        from_attributes = True

# ORM Model for EmergencyContact
class EmergencyContact(Base):
    __tablename__ = "emergency_contacts"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    profile_id = Column(UUID(as_uuid=True), ForeignKey('profiles.id'))
    contact_name = Column(String)
    contact_phone_number = Column(String)
    contact_relationship = Column(String)

    profile = relationship("Profile", backref="emergency_contacts")

    class Config:
        orm_mode = True
        from_attributes = True

    
# alembic revision -m ""
# alembic upgrade head
# alembic stamp head ( for changing the direct)