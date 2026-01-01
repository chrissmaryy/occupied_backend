# reservation_rules.py

# Welche Reservation-Typen blockieren welche anderen Typen
BLOCK_MAP = {
    "Duschen": ["Duschen", "Zähne putzen", "Toilette kurz", "Toilette lang"],
    "Zähne putzen": ["Duschen", "Toilette lang"],
    "Toilette kurz": ["Duschen", "Toilette kurz", "Toilette lang"],
    "Toilette lang": ["Duschen", "Zähne putzen", "Toilette kurz", "Toilette lang"]
}

def can_book(new_type: str, existing_types: list[str]) -> bool:
    """
    Prüft, ob new_type in Gegenwart von existing_types erlaubt ist.
    """
    blocked = BLOCK_MAP.get(new_type, [])
    for t in existing_types:
        if t in blocked:
            return False
    return True