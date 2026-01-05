from datetime import datetime, timedelta
from app.db.db_manager import *
from app.db.reservation_rules import *

def create_reservation(user_id: int, start: datetime, end: datetime, is_private: bool) -> int:
    now = datetime.now()
    
    reservation_id = create_reservation_entry(
        user_id,
        is_private,
        start,
        end
        )
    
    return(reservation_id)

def get_reservation(reservation_id: int):
    return get_reservation_by_id(reservation_id)

def get_reservations_per_day(day: datetime):
    return get_reservations_for_day(day.date().isoformat())

def get_reservations_per_user(user_id: int):
    return get_reservations_user(user_id)

def update_reservation(reservation_id: int, is_private: bool, start_time: datetime, end_time: datetime):
    return update_reservation_entry(
        reservation_id, 
        is_private, 
        start_time,
        end_time
    )

def delete_reservation(reservation_id: int, user_id: int):
    if not can_edit(reservation_id, user_id):
        raise PermissionError("Not your reservation")
    delete_reservation_entry(reservation_id)

def start_reservation_early(reservation_id: int, user_id: int):
    reservation = get_reservation_by_id(reservation_id)
    if not reservation:
        raise ValueError("Reservation not found")
    if not can_edit(reservation_id, user_id):
        raise PermissionError("Not your reservation")

    now = datetime.now()

    # Konfliktcheck
    conflicts = get_reservations_between(
        now,
        reservation["start_time"]
    )

    if conflicts:
        raise ValueError("Cannot start early, time blocked")
    
    delta = reservation["start_time"] - now
    new_end = reservation["end_time"] - delta

    update_reservation(
        reservation_id,
        reservation["is_private"],
        start_time=now,
        end_time=new_end
    )

def extend_reservation(reservation_id: int, user_id: int, extension_minutes: int):
    reservation = get_reservation_by_id(reservation_id)
    if not reservation:
        raise ValueError("Reservation not found")
    if not can_edit(reservation_id, user_id):
        raise PermissionError("Not your reservation")
    
    new_end_time = reservation["end_time"] + timedelta(minutes=extension_minutes)

    update_reservation(
        reservation_id,
        reservation["is_private"],
        reservation["start_time"],
        new_end_time
    )
    
def end_reservation_early(reservation_id: int, user_id: int):
    reservation = get_reservation_by_id(reservation_id)
    if not reservation:
        raise ValueError("Reservation not found")
    if not can_edit(reservation_id, user_id):
        raise PermissionError("Not your reservation")

    now = datetime.now()

    if not reservation["start_time"] <= now <= reservation["end_time"]:
        raise ValueError("Cannot end early, reservation not started")
    
    update_reservation(
        reservation_id,
        reservation["is_private"],
        reservation["start_time"],
        end_time=now
    )



