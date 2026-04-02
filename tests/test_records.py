from tests.conftest import get_token
from app.utils.enums import Role


def test_get_records(client, db):
    token = get_token(client, db, Role.VIEWER)

    response = client.get(
        "/records",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200


def test_create_record_permission_viewer(client, db):
    token = get_token(client, db, Role.VIEWER)

    response = client.post(
        "/records",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "amount": 100,
            "type": "INCOME",
            "category": "test",
            "date": "2026-04-01"
        }
    )

    # VIEWER should fail
    assert response.status_code == 403


def test_admin_can_create_record(client, db):
    token = get_token(client, db, Role.ADMIN)

    response = client.post(
        "/records",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "amount": 100,
            "type": "INCOME",
            "category": "test",
            "date": "2026-04-01"
        }
    )

    assert response.status_code == 200


def test_no_token_access(client):
    response = client.get("/records")

    assert response.status_code in [401, 403]