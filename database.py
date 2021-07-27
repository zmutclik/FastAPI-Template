from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from . import config
# from .models import rujukanModel,pesertaModel

DB_ENGINE = "mysql+pymysql://{1}:{2}@{0}/{3}"

engine_master = create_engine(DB_ENGINE.format(
    config.DB_URL,
    config.DB_USER,
    config.DB_PASS,
    config.DB_DATABASE))

SessionLocal = sessionmaker(autocommit=False, autoflush=False)
SessionLocal.configure(
    binds={  # rujukanModel.rujukan: engine_master,
    })


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
