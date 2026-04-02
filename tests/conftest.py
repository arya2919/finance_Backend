import os
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient

from app.main import app
from app.db.base import Base
from app.db.session import get_db

# 👉 TEST DATABASE
TEST_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    TEST_DATABASE_URL, connect_args={"check_same_thread": False}
)

TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)


# 🔥 Override dependency
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


# 🔥 Create + destroy DB per test session
@pytest.fixture(scope="session", autouse=True)
def setup_test_db():
    # Create tables
    Base.metadata.create_all(bind=engine)
    yield
    # Drop tables after tests
    Base.metadata.drop_all(bind=engine)

    # Delete file
    if os.path.exists("test.db"):
        os.remove("test.db")


@pytest.fixture()
def client():
    return TestClient(app)



def get_token(client, db, role):
    email = f"{role.value.lower() or 'user'}@gmail.com"

    client.post("/auth/register", json={
        "email": email,
        "password": "1234"
    })

    if role and db:
        from app.models.user import User
        user = db.query(User).filter(User.email == email).first()
        user.role = role
        db.commit()

    res = client.post("/auth/login", json={
        "email": email,
        "password": "1234"
    })

    return res.json()["access_token"]


@pytest.fixture()
def db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()