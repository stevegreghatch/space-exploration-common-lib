from pydantic import BaseModel


class Orbit(BaseModel):
    orbits: int
    apoapsis_km: int
    periapsis_km: int
    inclination_deg: int
    period_min: int

