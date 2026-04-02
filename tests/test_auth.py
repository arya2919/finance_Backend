

def test_register_success(client):
    response = client.post("/auth/register", json={
        "email": "test_auth@gmail.com",
        "password": "1234"
    })
    assert response.status_code == 200


def test_register_duplicate(client):
    client.post("/auth/register", json={
        "email": "dup@gmail.com",
        "password": "1234"
    })

    response = client.post("/auth/register", json={
        "email": "dup@gmail.com",
        "password": "1234"
    })

    assert response.status_code == 400


def test_login_success(client):
    client.post("/auth/register", json={
        "email": "login@gmail.com",
        "password": "1234"
    })

    response = client.post("/auth/login", json={
        "email": "login@gmail.com",
        "password": "1234"
    })

    assert response.status_code == 200
    assert "access_token" in response.json()


def test_login_wrong_password(client):
    client.post("/auth/register", json={
        "email": "wrong@gmail.com",
        "password": "1234"
    })

    response = client.post("/auth/login", json={
        "email": "wrong@gmail.com",
        "password": "9999"
    })

    assert response.status_code == 401


def test_invalid_email(client):
    response = client.post("/auth/register", json={
        "email": "invalid",
        "password": "1234"
    })

    assert response.status_code == 422

