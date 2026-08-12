from sqlalchemy import Column, Integer, String, Text, ForeignKey
from database import Base


# =========================
# USER TABLE
# =========================

class User(Base):
    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    username = Column(
        String(50),
        unique=True,
        nullable=False
    )

    email = Column(
        String(100),
        unique=True,
        nullable=False
    )

    password = Column(
        String(255),
        nullable=False
    )


# =========================
# ITINERARY TABLE
# =========================

class Itinerary(Base):
    __tablename__ = "itineraries"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    special_name = Column(
        String(150),
        nullable=True
    )

    title = Column(
        String(150),
        nullable=False
    )

    destination = Column(
        String(150),
        nullable=False
    )

    start_date = Column(
        String(30)
    )

    end_date = Column(
        String(30)
    )

    description = Column(
        Text
    )

    budget = Column(
        Integer,
        default=0
    )

    owner_id = Column(
        Integer,
        ForeignKey("users.id")
    )


# =========================
# ACTIVITY TABLE
# =========================

class Activity(Base):
    __tablename__ = "activities"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    itinerary_id = Column(
        Integer,
        ForeignKey("itineraries.id"),
        nullable=False
    )

    name = Column(
        String(150),
        nullable=False
    )

    location = Column(
        String(150)
    )

    date = Column(
        String(30)
    )

    description = Column(
        Text
    )