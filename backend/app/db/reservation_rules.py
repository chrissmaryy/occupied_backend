from app.db.db_manager import get_reservation_by_id
# Welche Reservation-Typen blockieren welche anderen Typen
BLOCK_MAP = {
    "Duschen": ["Duschen", "Zähne putzen", "Toilette kurz", "Toilette lang"],
    "Zähne putzen": ["Duschen", "Toilette lang"],
    "Toilette kurz": ["Duschen", "Toilette kurz", "Toilette lang"],
    "Toilette lang": ["Duschen", "Zähne putzen", "Toilette kurz", "Toilette lang"]
}

def can_book_type(new_reservation_type: int, existing_reservation_types: list[int]) -> bool:
    """
    Prüft, ob new_type in Gegenwart von existing_types erlaubt ist.
    """
    blocked = BLOCK_MAP.get(new_reservation_type, [])
    for t in existing_reservation_types:
        if t in blocked:
            return False
    return True

def overlaps(res_a: int, res_b: int) -> bool:
    reservation_a = get_reservation_by_id(res_a)
    reservation_b = get_reservation_by_id(res_b)
    return reservation_a["start_time"] < reservation_b["end_time"] and reservation_b["start_time"] < reservation_a["end_time"]

def can_edit(reservation_user_id: int, user_id: int) -> bool:
    if reservation_user_id == user_id:
        return True
    return False