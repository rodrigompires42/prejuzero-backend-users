from . import client

import json


def test_update_user_not_found():
    user_id = 999999999
    content = {
        "name": "new name",
        "phone": "11"
    }
    response = client.put(f"/api/v1/users/{user_id}", content=json.dumps(content))
    assert response.status_code == 404


def test_update_user_missing_parameters():
    user_id = 1
    content = {
        "name": "new name"
    }
    response = client.put(f"/api/v1/users/{user_id}", content=json.dumps(content))
    assert response.status_code == 422