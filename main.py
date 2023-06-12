from fastapi import FastAPI, Depends, Form
from sqlalchemy.orm import Session
import db.models as models
from db.database import engine, SessionLocal
from typing import Optional
from datetime import datetime

from swell.utils import get_swell
from wind.utils import get_wind


app = FastAPI()
models.Base.metadata.create_all(engine)

def get_session() -> Session:
    try:
        session = SessionLocal()
        yield session
    finally:
        session.close()

# Spots
@app.get("/spots")
def read_all_spots(session: Session = Depends(get_session)):
    return session.query(models.Spot).all()

@app.get("/spots/byname/")
def read_spot(spot_name: str, session: Session = Depends(get_session)):
    return session.query(models.Spot).filter(models.Spot.name == spot_name).all()

@app.post("/spots/add/")
def add_spot(name: str, region: str, country: str, exposition: str, sheltered_from: Optional[str] = None, session: Session = Depends(get_session)):
    exists = session.query(models.Spot).filter(models.Spot.name == name, models.Spot.region == region).first() is not None
    if exists:
        raise Exception("This spot has already been added")
    
    new_spot = models.Spot(
        name = name,
        region = region,
        country = country,
        exposition = exposition,
        sheltered_from = sheltered_from
    )
    session.add(new_spot)
    session.commit()

# Reports
@app.get("/reports")
def read_all_reports(session: Session = Depends(get_session)):
    return session.query(models.Report).all()

@app.get("/reports/add/")
def add_report(
    spot_id: int,
    rating: str,
    session: Session = Depends(get_session),
    comment: Optional[str] = None,
    report_at: Optional[datetime] = datetime.today(),
):
    
    swell_id = get_swell(spot_id, report_at, session)
    wind_id = get_wind(spot_id, report_at, session)

    new_report = models.Report(
        report_at = report_at,
        spot_id = spot_id,
        swell_id = swell_id,
        wind_id = wind_id,
        rating = rating,
        comment = comment,
    )
    session.add(new_report)
    session.commit()