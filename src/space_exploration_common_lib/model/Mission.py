from pydantic import BaseModel
from typing import List
from decimal import Decimal
from bson import Decimal128
from ..model.Duration import Duration


class Mission(BaseModel):
    mission: str
    astronauts: List[str]
    programs: str
    call_sign: str
    image_url: str
    spacecraft_number: int
    launch_time: str
    launch_site: str
    duration: Duration
    orbits: int
    apogee_mi: int
    perigee_mi: int
    velocity_max_mph: int
    miss_mi: Decimal

    def __init__(self, **data):
        if 'miss_mi' in data and isinstance(data['miss_mi'], Decimal128):
            data['miss_mi'] = Decimal(str(data['miss_mi']))
        super().__init__(**data)
