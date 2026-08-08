from sqlalchemy.orm import Session
from app.models.trip import Trip
from app.schemas.trip import TripCreate


def create_trip(db: Session, trip: TripCreate):
    db_trip = Trip(
        trip_name=trip.trip_name,
        source=trip.source,
        destination=trip.destination,
        days=trip.days
    )

    db.add(db_trip)
    db.commit()
    db.refresh(db_trip)

    return db_trip