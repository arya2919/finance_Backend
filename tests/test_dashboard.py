from tests.conftest import get_token
from app.utils.enums import Role



def test_dashboard_viewer_forbidden(client, db):
    token = get_token(client, db, Role.VIEWER)

    response = client.get(
        "/dashboard/summary",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 403


def test_dashboard_analyst_allowed(client, db):
    token = get_token(client, db, Role.ANALYST)

    response = client.get(
        "/dashboard/summary",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200


def test_dashboard_admin_allowed(client, db):
    token = get_token(client, db, Role.ADMIN)

    response = client.get(
        "/dashboard/summary",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200