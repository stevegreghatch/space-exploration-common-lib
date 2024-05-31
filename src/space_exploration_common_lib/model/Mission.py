from pydantic import BaseModel
from typing import List
from ..model.Duration import Duration


class Mission(BaseModel):
    mission: str
    astronauts: List[str]
    program: str
    call_sign: str
    image_url: str
    launch_mass_lbs: int
    launch_site: str
    launch_time: str
    launch_vehicle: str
    orbits: int
    apogee_mi: int
    perigee_mi: int
    velocity_max_mph: int
    landing_date: str
    landing_site: str
    recovery_ship: str
    duration: Duration
    distance_traveled: int
