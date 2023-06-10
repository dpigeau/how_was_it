from datetime import datetime
from db import models
from sqlalchemy.orm import Session

def get_swell(spot_id: int, report_at: datetime, db: Session):
    """Fetch swell from api and add it to database"""

    swell = models.Swell(
        swell_at = report_at,
        height = 6,
        direction = 225,
        period = 12,
    )
    db.add(swell)
    db.commit()

    return swell.id