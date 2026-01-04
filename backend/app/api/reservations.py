from fastapi import APIRouter, Depends, HTTPException
from app.models.schemas import *
from app.services.reservation_service import *
from datetime import date

router = APIRouter(prefix="/reservations", tags=["reservations"])

def get_current_user():
    return {"id": 1}

@router.post("/")
def create_reservation_endpoint(data: ReservationCreateRequest, current_user = Depends(get_current_user)):
    try:
        return create_reservation(
            current_user,
            data.start_time,
            data.end_time,
            data.type
        )
    except ValueError as e:
        raise HTTPException(status_code=400, details=str(e))

@router.get("/{id}")
def get_reservation_endpoint(reservation_id: int):
    try:
         reservation = get_reservation(reservation_id=reservation_id)
    except ValueError as e:
        raise HTTPException(status_code=400, details=str(e))
    
    if reservation is None:
        return HTTPException(status_code=404, details="Reservation not found")
    return reservation

@router.get("/")
def get_reservations_for_day_endpoint(date:date):
    return get_reservations_per_day(date)

@router.get("/")
def get_reservation_for_user_endpoint(current_user = Depends(get_current_user)):
    if current_user is None:
        raise HTTPException(status_code=400, details=str(e))

    try:
        return get_reservations_per_user(current_user)
    except ValueError as e:
        raise HTTPException(status_code=400, details=str(e))

@router.put("/{id}")
def update_reservation_endpoint(reservation_id: int, data: ReservationUpdateRequest):
    try:
         reservation = update_reservation(
            reservation_id,
            data.type,
            data.start_time,
            data.end_time
        )
    except ValueError as e:
        raise HTTPException(status_code=400, details=str(e))
    
    if reservation is None:
        return HTTPException(status_code=404, details="Reservation not found")
    return reservation

@router.delete("/{id}")
def delete_reservation_endpoint(reservation_id: int, current_user = Depends(get_current_user)):
    try:
         reservation = delete_reservation(
            reservation_id, 
            current_user["id"]
        )
    except ValueError as e:
        raise HTTPException(status_code=400, details=str(e))
    
    if reservation is None:
        return HTTPException(status_code=404, details="Reservation not found")
    return {"status": "ok"}

@router.post("/{id}/start-early")
def start_reservation_early_endpoint(reservation_id: int, current_user = Depends(get_current_user)):
    try:
         reservation = start_reservation_early(
            reservation_id, 
            current_user["id"]
        )
    except ValueError as e:
        raise HTTPException(status_code=400, details=str(e))
    
    if reservation is None:
        return HTTPException(status_code=404, details="Reservation not found")
    return reservation

@router.post("/{id}/extend")
def extend_reservation_endpoint(reservation_id: int, data: ReservationExtendRequest, current_user = Depends(get_current_user)):
    try:
         reservation = extend_reservation(
            reservation_id, 
            current_user["id"], 
            data.minutes
        )
    except ValueError as e:
        raise HTTPException(status_code=400, details=str(e))
    
    if reservation is None:
        return HTTPException(status_code=404, details="Reservation not found")
    return reservation

@router.post("/{id}/end-early")
def end_reservation_early_endpoint(reservation_id: int, current_user = Depends(get_current_user)):
    try:
         reservation = end_reservation_early(
            reservation_id,
            current_user
        )
    except ValueError as e:
        raise HTTPException(status_code=400, details=str(e))
    
    if reservation is None:
        return HTTPException(status_code=404, details="Reservation not found")
    return reservation
    