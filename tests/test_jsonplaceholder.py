import requests
import pytest


def test_get_posts_returns_200(base_url):
    r = requests.get(f"{base_url}/posts")
    assert r.status_code == 200


def test_get_posts_returns_list(base_url):
    r = requests.get(f"{base_url}/posts")
    data = r.json()
    assert isinstance(data, list)
    assert len(data) > 0


def test_get_single_post(base_url):
    r = requests.get(f"{base_url}/posts/1")
    assert r.status_code == 200
    data = r.json()
    assert data["id"] == 1
    assert "title" in data
    assert "body" in data


def test_create_post(base_url):
    payload = {"title": "Test Post", "body": "Test body", "userId": 1}
    r = requests.post(f"{base_url}/posts", json=payload)
    assert r.status_code == 201
    data = r.json()
    assert data["title"] == payload["title"]
    assert "id" in data


def test_update_post(base_url):
    payload = {"id": 1, "title": "Updated Title", "body": "Updated body", "userId": 1}
    r = requests.put(f"{base_url}/posts/1", json=payload)
    assert r.status_code == 200
    data = r.json()
    assert data["title"] == "Updated Title"


def test_delete_post(base_url):
    r = requests.delete(f"{base_url}/posts/1")
    assert r.status_code == 200


@pytest.mark.parametrize("post_id", [1, 2, 3, 50, 100])
def test_get_post_by_id(base_url, post_id):
    r = requests.get(f"{base_url}/posts/{post_id}")
    assert r.status_code == 200
    data = r.json()
    assert data["id"] == post_id


@pytest.mark.parametrize("post_id", [0, -1, 99999, 999999])
def test_invalid_post_id_returns_404(base_url, post_id):
    r = requests.get(f"{base_url}/posts/{post_id}")
    assert r.status_code == 404


@pytest.mark.parametrize("post_id,expected_status", [
    (1,     200),
    (100,   200),
    (101,   404),   # doesn't exist
    (-1,    404),
])
def test_get_post_status(base_url, post_id, expected_status):
    r = requests.get(f"{base_url}/posts/{post_id}")
    assert r.status_code == expected_status


@pytest.mark.parametrize("user_id,expected_status", [
    (1,     200),
    (2,   200),
    (11,   404),   # doesn't exist
    (-1,    404),
])
def test_get_user_status(base_url, user_id, expected_status):
    r = requests.get(f"{base_url}/users/{user_id}")
    assert r.status_code == expected_status
