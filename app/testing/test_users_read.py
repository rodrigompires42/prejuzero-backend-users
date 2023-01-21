from . import client


def test_read_all_users():
    response = client.get("/api/v1/users")
    assert response.status_code == 200
    

def test_read_one_user():
    response = client.get("/api/v1/users/1")
    assert response.status_code == 200


def test_read_one_user_not_found():
    user_id = 999999999
    response = client.get(f"/api/v1/users/{user_id}")
    assert response.status_code == 404
    assert response.json() == {
        "detail": f"User with the id {user_id} is not available"
    }