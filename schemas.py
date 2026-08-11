from pydantic import BaseModel, EmailStr


# =========================
# USER
# =========================

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        from_attributes = True



# =========================
# ITINERARY
# =========================

class ItineraryCreate(BaseModel):

    special_name: str | None = None

    title: str

    destination: str

    start_date: str | None = None

    end_date: str | None = None

    description: str | None = None

    budget: int = 0



class ItineraryResponse(BaseModel):

    id: int

    special_name: str | None

    title: str

    destination: str

    start_date: str | None

    end_date: str | None

    description: str | None

    budget: int

    owner_id: int | None


    class Config:
        from_attributes = True