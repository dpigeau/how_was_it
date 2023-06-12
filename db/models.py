from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import ForeignKey
from sqlalchemy.sql import func
from datetime import datetime
from typing import Optional

class Base(DeclarativeBase):
    pass

class Spot(Base):
    __tablename__ = "spots"

    id: Mapped[int] = mapped_column(primary_key=True)
    surfline_id: Mapped[str]
    name: Mapped[str]
    region: Mapped[str]
    country: Mapped[str]
    exposition: Mapped[str]
    sheltered_from: Mapped[Optional[str]] = mapped_column(server_default=None)

    def __repr__(self) -> str:
        return F"<name: {self.name}, exposition: {self.exposition}, sheltered_from: {self.sheltered_from}"
    
class Swell(Base):
    __tablename__ = "swells"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement="auto")
    swell_at: Mapped[datetime]
    height: Mapped[int]
    direction: Mapped[float]
    directionMin: Mapped[float]
    period: Mapped[int]
    power: Mapped[float]
    impact: Mapped[int]
    optimalScore: Mapped[int]
    created_at: Mapped[Optional[datetime]] = mapped_column(server_default=func.now())

    def __repr__(self) -> str:
        return F"<size: {self.height}, direction: {self.direction}, period: {self.period}, created_at: {self.created_at}"

class Wind(Base):
    __tablename__ = "winds"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement="auto")
    wind_at: Mapped[datetime]
    speed: Mapped[float]
    gust: Mapped[float]
    direction: Mapped[float]
    directionType: Mapped[str]
    optimalScore: Mapped[int]
    created_at: Mapped[Optional[datetime]] = mapped_column(server_default=func.now())

    def __repr__(self) -> str:
        return F"<speed: {self.strength}, direction: {self.direction}, created_at: {self.created_at}"
    
class Tide(Base):
    __tablename__ = "tides"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement="auto")
    tide_at: Mapped[datetime]
    height: Mapped[float]
    type: Mapped[str]

class Report(Base):
    __tablename__ = "reports"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement="auto")
    report_at: Mapped[datetime]
    spot_id: Mapped[int] = mapped_column(ForeignKey("spots.id"))
    swell_id: Mapped[int] = mapped_column(ForeignKey("swells.id"))
    wind_id: Mapped[int] = mapped_column(ForeignKey("winds.id"))
    tide_id: Mapped[str]  = mapped_column(ForeignKey("tides.id"))
    rating: Mapped[int]
    comment: Mapped[str] = mapped_column(nullable=True)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now())