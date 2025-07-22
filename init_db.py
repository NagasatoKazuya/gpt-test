import models
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

def main():
    db = SessionLocal()
    if db.query(models.Candidate).count() == 0:
        names = ["Alice", "Bob", "Charlie"]
        for name in names:
            db.add(models.Candidate(name=name))
        db.commit()
    db.close()

if __name__ == "__main__":
    main()
