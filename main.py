from fastapi import FastAPI, Depends, Form
from sqlalchemy.orm import Session
import db.models as models
from db.database import engine, SessionLocal
from typing import Optional
from datetime import datetime

from surfline.surflineForecast import SurflineForecast

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

# @app.get("/spots/byname/")
# def read_spot(spot_name: str, session: Session = Depends(get_session)):
#     return session.query(models.Spot).filter(models.Spot.name == spot_name).all()

@app.post("/spots/add/")
def add_spot(surfline_id:str, name: str, region: str, country: str, exposition: str, sheltered_from: Optional[str] = None, session: Session = Depends(get_session)):
    exists = session.query(models.Spot).filter(models.Spot.name == name, models.Spot.region == region).first() is not None
    if exists:
        raise Exception("This spot has already been added")
    
    new_spot = models.Spot(
        surfline_id = surfline_id,
        name = name,
        region = region,
        country = country,
        exposition = exposition,
        sheltered_from = sheltered_from
    )
    session.add(new_spot)
    session.commit()

# Swells
@app.get("/swells")
def read_all_swells(session: Session = Depends(get_session)):
    return session.query(models.Swell).all()

# Winds
@app.get("/winds")
def read_all_swells(session: Session = Depends(get_session)):
    return session.query(models.Wind).all()

# Tides
@app.get("/tides")
def read_all_swells(session: Session = Depends(get_session)):
    return session.query(models.Tide).all()

# Reports
@app.get("/reports")
def read_all_reports(session: Session = Depends(get_session)):
    return session.query(models.Report).all()

@app.get("/reports/add/")
def add_report(
    spot_id: str,
    rating: str,
    comment: Optional[str] = None,
    report_at: Optional[datetime] = datetime.today(),
    session: Session = Depends(get_session),
):
    
    forecast = SurflineForecast(spot_id, report_at)
    
    swell = models.Swell(**forecast.swell())
    session.add(swell)

    wind = models.Wind(**forecast.wind())
    session.add(wind)

    tide = models.Tide(**forecast.tide())
    session.add(tide)

    session.commit()
    new_report = models.Report(
        report_at = report_at,
        spot_id = spot_id,
        swell_id = swell.id,
        wind_id = wind.id,
        tide_id = tide.id,
        rating = rating,
        comment = comment,
    )
    session.add(new_report)
    session.commit()