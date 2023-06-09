from fastapi import FastAPI, Depends, Form
from sqlalchemy.orm import Session
import howwasit.models as models
from howwasit.database import engine, SessionLocal
from typing import Optional


app = FastAPI()
models.Base.metadata.create_all(engine)

def get_db() -> Session:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/spots")
def read_all_spots(db: Session = Depends(get_db)):
    return db.query(models.Spot).all()

@app.get("/spots/byname/")
def read_spot(spot_name: str, db: Session = Depends(get_db)):
    return db.query(models.Spot).filter(models.Spot.name == spot_name).all()

@app.post("/spots/add/")
def add_spot(name: str, exposition: str, sheltered_from: Optional[str] = None, db: Session = Depends(get_db)):
    new_spot = models.Spot(
        name = name,
        exposition = exposition,
        sheltered_from = sheltered_from
    )
    db.add(new_spot)
    db.commit()

# @app.get("/reports")
# def read_all_reports(db: Session = Depends(get_db)):
#     return db.query(models.Report).all()

# @app.get("/reports/{spot_name}")
# def read_reports(db: Session = Depends(get_db)):
#     return db.query(models.Report).join...