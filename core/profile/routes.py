from fastapi import APIRouter,HTTPException,Depends
from sqlalchemy.orm import Session
from dependencies import get_db,get_current_user
from core.user.models import User
from .models import Profile,Doctor,EmergencyContact
from .schema import ProfileCreate,DoctorCreate,EmergencyContactCreate

profile_router=APIRouter()

def get_profile_id_from_user_id(db: Session, user_id: str) -> str:
    """
    Fetches the profile_id based on user_id.
    """
    profile = db.query(Profile).filter(Profile.user_id == user_id).first()
    if profile:
        return profile.id
    return None

@profile_router.post('/profile')
def create_profile(profile_data: ProfileCreate, db: Session = Depends(get_db), user:User =Depends(get_current_user)):
    try:
        new_profile = Profile(dob=profile_data.dob,gender=profile_data.gender,appointment_frequency=profile_data.appointment_frequency,user_id=user.id)
        db.add(new_profile)
        db.commit()
        db.refresh(new_profile)
        return {"message": "Profile has been created"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error occurred: {str(e)}")

@profile_router.post('/doctor_details')
def create_doctor(doctor_data: DoctorCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    try:
        # Assuming you have a function to fetch the profile_id based on user_id
        profile_id = get_profile_id_from_user_id(db, user.id)
        
        if profile_id is None:
            raise HTTPException(status_code=404, detail="Profile not found for the current user")

        new_doctor = Doctor(
            name=doctor_data.name,
            phone_number=doctor_data.phone_number,
            clinic_or_hospital_name=doctor_data.clinic_or_hospital_name,
            email=doctor_data.email,
            profile_id=profile_id
        )
        db.add(new_doctor)
        db.commit()
        return {"message": "Doctor details have been created"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error occurred: {str(e)}")


@profile_router.post('/emergency_contact')
def create_emergency_contact(emer_data: EmergencyContactCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    try:
        # Assuming you have a function to fetch the profile_id based on user_id
        profile_id = get_profile_id_from_user_id(db, user.id)
        
        if profile_id is None:
            raise HTTPException(status_code=404, detail="Profile not found for the current user")

        new_contact = EmergencyContact(
            contact_name=emer_data.contact_name,
            contact_phone_number=emer_data.contact_phone_number,
            contact_relationship=emer_data.contact_relationship,
            profile_id=profile_id
        )
        db.add(new_contact)
        db.commit()
        return {"message": "Emergency Contact details have been created"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error occurred: {str(e)}")
    
@profile_router.get("/user_details")
def get_user_details(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return user

@profile_router.get("/profile_details", response_model=dict)
async def get_profile_details(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    try:
        profile = db.query(Profile).filter(Profile.user_id == user.id).first()
        if not profile:
            raise HTTPException(status_code=404, detail="Profile not found for the current user")

        doctor = db.query(Doctor).filter(Doctor.profile_id == profile.id).first()
        emergency_contact = db.query(EmergencyContact).filter(EmergencyContact.profile_id == profile.id).first()

        response_data = {
            "profile": {
                "id": str(profile.id),
                "dob": profile.dob,
                "gender": profile.gender,
                "appointment_frequency": profile.appointment_frequency,
                "user_id": str(profile.user_id)
            },
            "doctor": None,
            "emergency_contact": None
        }

        if doctor:
            response_data["doctor"] = {
                "id": str(doctor.id),
                "name": doctor.name,
                "phone_number": doctor.phone_number,
                "clinic_or_hospital_name": doctor.clinic_or_hospital_name,
                "email": doctor.email,
                "profile_id": str(doctor.profile_id)
            }

        if emergency_contact:
            response_data["emergency_contact"] = {
                "id": str(emergency_contact.id),
                "contact_name": emergency_contact.contact_name,
                "contact_phone_number": emergency_contact.contact_phone_number,
                "contact_relationship": emergency_contact.contact_relationship,
                "profile_id": str(emergency_contact.profile_id)
            }

        return response_data

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error occurred: {str(e)}")
    
@profile_router.delete("/delete_profile")
async def delete_entity(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    try:
        profile = db.query(Profile).filter(Profile.user_id == user.id).first()
        if not profile:
            raise HTTPException(status_code=404, detail="Profile not found for the current user")

        doctor = db.query(Doctor).filter(Doctor.profile_id == profile.id).first()
        emergency_contact = db.query(EmergencyContact).filter(EmergencyContact.profile_id == profile.id).first()

        if profile:
            db.delete(profile)
        if doctor:
            db.delete(doctor)
        if emergency_contact:
            db.delete(emergency_contact)

        db.commit()

        return {"message": "Profile and associated records deleted successfully"}

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error occurred: {str(e)}")