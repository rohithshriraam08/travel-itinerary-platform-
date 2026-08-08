from pydantic import BaseModel


class TripCreate(BaseModel):
    trip_name: str
    source: str
    destination: str
    days: int