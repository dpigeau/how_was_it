import howwasit.models as models
from howwasit.database import engine, SessionLocal
from sqlalchemy import Select

models.Base.metadata.create_all(engine)

with SessionLocal() as session:
    llandudno = models.Spot(
        name = "llandudno",
        exposition = "west",
        sheltered_from = "north-west"
    )

    the_dunes = models.Spot(
        name = "the dunes",
        exposition = "west"
    )
    session.add_all([llandudno, the_dunes])
    session.commit()

    #print
    q = Select(models.Spot)
    print(type(q))
    for s in session.scalars(q):
        print(s)

    