from sqlalchemy import Column, Integer, String
from app.core.database import Base


class Trip(Base):
    __tablename__ = "trips"

    id = Column(Integer, primary_key=True, index=True)
    trip_name = Column(String(100), nullable=False)
    source = Column(String(100), nullable=False)
    destination = Column(String(100), nullable=False)
    days = Column(Integer, nullable=False)