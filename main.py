from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal, engine, Base
from models import User, Itinerary, Activity
from schemas import (
    UserCreate,
    UserLogin,
    ItineraryCreate,
    ActivityCreate
)


# Create database tables
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Travel Itinerary Planning and Sharing Platform",
    description="Backend API for creating, managing and sharing travel plans",
    version="1.0.0"
)


# Database connection
def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()



# =========================
# SYSTEM
# =========================

@app.get(
    "/",
    tags=["System"],
    summary="API Welcome Message"
)
def root():

    return {
        "message": "Welcome to Travel Itinerary Platform API"
    }



@app.get(
    "/health",
    tags=["System"],
    summary="Check API Health"
)
def health():

    return {
        "status": "OK"
    }



# =========================
# USER MANAGEMENT
# =========================


@app.post(
    "/register",
    tags=["User Management"],
    summary="Register New User"
)
def register(
    user_data: UserCreate,
    db: Session = Depends(get_db)
):

    existing_user = db.query(User).filter(
        User.email == user_data.email
    ).first()


    if existing_user:

        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )


    user = User(
        username=user_data.username,
        email=user_data.email,
        password=user_data.password
    )


    db.add(user)
    db.commit()
    db.refresh(user)


    return {

        "message": "User registered successfully",
        "user_id": user.id

    }




@app.post(
    "/login",
    tags=["User Management"],
    summary="User Login"
)
def login(
    user_data: UserLogin,
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(
        User.email == user_data.email,
        User.password == user_data.password
    ).first()


    if not user:

        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )


    return {

        "message": "Login successful",
        "user_id": user.id,
        "username": user.username

    }




# =========================
# ITINERARY MANAGEMENT
# =========================


@app.post(
    "/itineraries",
    tags=["Itinerary Management"],
    summary="Create New Travel Plan"
)
def create_itinerary(
    itinerary_data: ItineraryCreate,
    owner_id: int,
    db: Session = Depends(get_db)
):

    itinerary = Itinerary(

        special_name=itinerary_data.special_name,
        title=itinerary_data.title,
        destination=itinerary_data.destination,
        start_date=itinerary_data.start_date,
        end_date=itinerary_data.end_date,
        description=itinerary_data.description,
        budget=itinerary_data.budget,
        owner_id=owner_id

    )


    db.add(itinerary)
    db.commit()
    db.refresh(itinerary)


    return {

        "message": "Travel plan created successfully",
        "itinerary_id": itinerary.id

    }




@app.get(
    "/itineraries",
    tags=["Itinerary Management"],
    summary="View All Travel Plans"
)
def get_all_travel_plans(
    db: Session = Depends(get_db)
):

    return db.query(Itinerary).all()




@app.get(
    "/itineraries/{itinerary_id}",
    tags=["Itinerary Management"],
    summary="View Travel Plan Details"
)
def get_travel_plan_details(
    itinerary_id: int,
    db: Session = Depends(get_db)
):

    itinerary = db.query(Itinerary).filter(
        Itinerary.id == itinerary_id
    ).first()


    if not itinerary:

        raise HTTPException(
            status_code=404,
            detail="Travel plan not found"
        )


    return itinerary




@app.delete(
    "/itineraries/{itinerary_id}",
    tags=["Itinerary Management"],
    summary="Remove Travel Plan"
)
def remove_travel_plan(
    itinerary_id: int,
    db: Session = Depends(get_db)
):

    itinerary = db.query(Itinerary).filter(
        Itinerary.id == itinerary_id
    ).first()


    if not itinerary:

        raise HTTPException(
            status_code=404,
            detail="Travel plan not found"
        )


    db.delete(itinerary)
    db.commit()


    return {

        "message": "Travel plan removed successfully"

    }




# =========================
# ACTIVITY MANAGEMENT
# =========================


@app.post(
    "/activities",
    tags=["Activity Management"],
    summary="Create Activity"
)
def create_activity(
    activity_data: ActivityCreate,
    db: Session = Depends(get_db)
):

    activity = Activity(

        itinerary_id=activity_data.itinerary_id,
        name=activity_data.name,
        location=activity_data.location,
        date=activity_data.date,
        description=activity_data.description

    )


    db.add(activity)
    db.commit()
    db.refresh(activity)


    return {

        "message": "Activity created successfully",
        "activity_id": activity.id

    }




@app.get(
    "/activities",
    tags=["Activity Management"],
    summary="View All Activities"
)
def get_all_activities(
    db: Session = Depends(get_db)
):

    return db.query(Activity).all()




@app.get(
    "/activities/{activity_id}",
    tags=["Activity Management"],
    summary="View Activity Details"
)
def get_activity(
    activity_id: int,
    db: Session = Depends(get_db)
):

    activity = db.query(Activity).filter(
        Activity.id == activity_id
    ).first()


    if not activity:

        raise HTTPException(
            status_code=404,
            detail="Activity not found"
        )


    return activity




@app.delete(
    "/activities/{activity_id}",
    tags=["Activity Management"],
    summary="Remove Activity"
)
def remove_activity(
    activity_id: int,
    db: Session = Depends(get_db)
):

    activity = db.query(Activity).filter(
        Activity.id == activity_id
    ).first()


    if not activity:

        raise HTTPException(
            status_code=404,
            detail="Activity not found"
        )


    db.delete(activity)
    db.commit()


    return {

        "message": "Activity removed successfully"

    }