from datetime import datetime
from db import models
from sqlalchemy.orm import Session

def get_wind(spot_id: int, report_at: datetime, db: Session):
    """Fetch swell from api and add it to database"""

    wind = models.Wind(
        wind_at = report_at,
        speed = 2,
        direction = 90,
    )
    db.add(wind)
    db.commit()

    return wind.id