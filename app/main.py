from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from app.db.session import engine
from app.models import user, financial_record
from app.api import api_router
from app.db.base import Base


app = FastAPI(
    title="Zorvyn Finance API",
    description="Backend system with RBAC, financial records, and analytics",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

app.include_router(api_router)


@app.get("/")
def root():
    return RedirectResponse(url="/docs")
