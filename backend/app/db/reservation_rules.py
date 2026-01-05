from app.db.db_manager import get_reservation_by_id

def overlaps(res_a: int, res_b: int) -> bool:
    reservation_a = get_reservation_by_id(res_a)
    reservation_b = get_reservation_by_id(res_b)
    return reservation_a["start_time"] < reservation_b["end_time"] and reservation_b["start_time"] < reservation_a["end_time"]

def can_edit(reservation_user_id: int, user_id: int) -> bool:
    if reservation_user_id == user_id:
        return True
    return False