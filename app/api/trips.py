from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.trip import TripCreate
from app.services.trip_service import create_trip

router = APIRouter(
    prefix="/trips",
    tags=["Trips"]
)


@router.post("/")
def add_trip(trip: TripCreate, db: Session = Depends(get_db)):
    return create_trip(db, trip)