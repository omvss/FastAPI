from app import models

from app.config import settings
from fastapi import FastAPI
from app.database import Base, engine
from app.routes import category, sub_category



models.Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.APP_NAME)

app.include_router(category.router)
app.include_router(sub_category.router)