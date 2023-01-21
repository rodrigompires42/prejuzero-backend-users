import json
import random
import string

from . import client


def test_create_user():
    random_email = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
    new_user = {
        "name": "Test User",
        "email": f"{random_email}@email.com",
        "password": "password",
        "phone": "1191289237"
    }
    response = client.post("/api/v1/users", content=json.dumps(new_user))
    assert response.status_code == 202


def test_create_user_missing_parameters():
    new_user = {
        "name": "Test User",
        "password": "password",
        "phone": "1191289237"
    }
    response = client.post("/api/v1/users", content=json.dumps(new_user))
    assert response.status_code == 422


def test_create_user_email_already_in_use():
    new_user = {
        "name": "Test User",
        "email": "test@email.com",
        "password": "password",
        "phone": "1191289237"
    }
    response = client.post("/api/v1/users", content=json.dumps(new_user))
    assert response.status_code == 409