from pydantic import BaseModel
from datetime import datetime

class ReservationCreateRequest(BaseModel):
    start_time: datetime
    end_time: datetime
    type: int

class ReservationUpdateRequest(BaseModel):
    start_time: datetime | None = None
    end_time: datetime | None = None
    type: int | None = None

class ReservationExtendRequest(BaseModel):
    minutes: int