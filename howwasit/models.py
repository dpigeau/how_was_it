from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import ForeignKey
from sqlalchemy.sql import func
from datetime import datetime
from typing import Optional

class Base(DeclarativeBase):
    pass

class Spot(Base):
    __tablename__ = "spots"

    id : Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    exposition: Mapped[str]
    sheltered_from: Mapped[Optional[str]] = mapped_column(server_default=None)

    def __repr__(self) -> str:
        return F"<name: {self.name}, exposition: {self.exposition}, sheltered_from: {self.sheltered_from}"
    
class Swell(Base):
    __tablename__ = "swells"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement="auto")
    height: Mapped[int]
    direction: Mapped[int]
    period: Mapped[int]
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    def __repr__(self) -> str:
        return F"<size: {self.height}, direction: {self.direction}, period: {self.period}, created_at: {self.created_at}"

class Wind(Base):
    __tablename__ = "winds"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement="auto")
    speed: Mapped[int]
    direction: Mapped[int]
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    def __repr__(self) -> str:
        return F"<speed: {self.strength}, direction: {self.direction}, created_at: {self.created_at}"

class Report(Base):
    __tablename__ = "reports"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement="auto")
    spot_id: Mapped[int] = mapped_column(ForeignKey("spots.id"))
    swell_id: Mapped[int] = mapped_column(ForeignKey("swells.id"))
    wind_id: Mapped[int] = mapped_column(ForeignKey("winds.id"))
    rating: Mapped[str]
    comment: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now())