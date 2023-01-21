from . import client


def test_delete_user_not_existing():
    user_id = 999999999
    response = client.delete(f"/api/v1/users?id={user_id}")
    assert response.status_code == 404